from Adafruit_IO import MQTTClient
from datetime import datetime
from abc import ABC, abstractmethod
import time 
from .adafruit import Adafruit
from .command import waterModify, smartFarmController, lightingModify, temperatureModify
from ..collection.humid_collection import humid_collection
from ..collection.light_collection import light_collection
from ..collection.temperature_collection import temperature_collection
from ...collection.notification_collection import notification_collection
from ...services.socketio_service import emit_sensor_data


def get_mode(device: str) -> str:
  with open("/home/khoitrananh/working/CO3109/greensense_be/iot_env.txt", 'r') as fopen:
    current_modes = eval(fopen.read())
  
  if device not in current_modes:
    return ""
  
  return current_modes[device]

class sensorManager:
  
  __listener: dict
  def __init__(self):
    self.__listener = dict()

  def subscribe(self, eventType, listener):
    self.__listener[eventType] = listener

  def unsubscribe(self, eventType):
    del self.__listener[eventType]
  
  def notify(self, eventType, data):
    self.__listener[eventType].update(data)

    log_data = {
      'time': datetime.now(),
      'event_type': eventType,
      'data': data
    }

    # Emit to WebSocket clients
    emit_sensor_data(eventType, data, log_data['time'])

    # Check for notification rules
    active_notifications = notification_collection.find({'event_type': eventType, 'is_active': True})
    for rule in active_notifications:
        threshold = rule['threshold']
        condition = rule['condition']
        message = rule['message']

        if (condition == 'greater_than' and int(data) > threshold) or \
           (condition == 'less_than' and int(data) < threshold):
            emit_sensor_data('notification', message, log_data['time'])

    self.__listener['log'].update(log_data)

class Sensor:
  sensor: sensorManager
  __client: Adafruit

  def __init__(self, config):
    
    self.sensor = sensorManager()
    self.__client = Adafruit(config['ADAFRUIT_IO_USERNAME'], config['ADAFRUIT_IO_KEY'], config['IOT_GADGET'])
    self.__client.start()

    for feed_id in self.__client.getFeeds():
      if feed_id[0] == 'humid':
        self.sensor.subscribe(feed_id[0], humidListener(feed_id[0], feed_id[1], self.__client))
      elif feed_id[0] == 'temperature':
        self.sensor.subscribe(feed_id[0], temperatureListener(feed_id[0], feed_id[1], self.__client))
      elif feed_id[0] == 'light-sensor':
        self.sensor.subscribe(feed_id[0], lightingListener(feed_id[0], feed_id[1], self.__client))

    self.sensor.subscribe('log', logListener())

  def start_receive(self):
    while True:
      # time.sleep(20)
      datas = self.__client.get_message_queue()

      # (feed_id, payload)
      while len(datas) != 0:
        if datas[0][0] == 'humid':
          self.updateHumidData(datas[0][1])

        elif datas[0][0] == 'temperature':
          self.updateTemparatureData(datas[0][1])

        elif datas[0][0] == 'light-sensor':
          self.updateLightingData(datas[0][1])

        self.__client.pop_message_queue()

  def updateHumidData(self, data):
    self.sensor.notify('humid', data)
  
  def updateTemparatureData(self, data):
    self.sensor.notify('temperature', data)

  def updateLightingData(self, data):
    self.sensor.notify('light-sensor', data)

class sensorListener(ABC):
  _client: Adafruit
  _feed_gadget_modify: str
  _feed_sensor: str
  _controller: smartFarmController

  def __init__(self, feed_sensor, feed_gadget_modify, client: Adafruit):
    self._controller = smartFarmController()
    self._feed_gadget_modify = feed_gadget_modify
    self._client = client
    self._feed_sensor = feed_sensor

  @abstractmethod
  def update(self, data):
    pass

class logListener(sensorListener):
  def __init__(self):
    pass

  def update(self, data):
    document = {
      "time": data['time'],
      "data": int(data['data'])
    }
    event_type = data['event_type']
    
    if event_type == 'humid':
      humid_collection.insert_one(document)
    elif event_type == 'temperature':
      temperature_collection.insert_one(document)
    elif event_type == 'light-sensor':
      light_collection.insert_one(document)


class humidListener(sensorListener):
  def __init__(self, feed_sensor, feed_gadget_modify, client: Adafruit):
    super().__init__(feed_sensor, feed_gadget_modify, client)


  def update(self, data):
    
    # tạo ra 1 đối tượng để điều chỉnh humid listener

    # logic điều chỉnh độ ẩm như thế nào thì bỏ vào đây
    if get_mode('pump') == 'automatic' and int(data) < 50:
      # Turn on water pump
      update_data = 1
      self._controller.add_command(waterModify(self._client, self._feed_gadget_modify, update_data))
      self._controller.excute_command()
      
      # Turn off water pump
      time.sleep(20)
      update_data = 0
      self._controller.add_command(waterModify(self._client, self._feed_gadget_modify, update_data))
      self._controller.excute_command()

    
class temperatureListener(sensorListener):

  def __init__(self, feed_sensor, feed_gadget_modify, client: Adafruit):
    super().__init__(feed_sensor, feed_gadget_modify, client)

  def update(self, data):  
    if get_mode('servo') != 'automatic':
      return
    
    if int(data) > 60:
      servo_angle = 180
      self._controller.add_command(temperatureModify(self._client, self._feed_gadget_modify, servo_angle))
      self._controller.excute_command()
    elif int(data) < 40:
      servo_angle = 0
      self._controller.add_command(temperatureModify(self._client, self._feed_gadget_modify, servo_angle))
      self._controller.excute_command()



class lightingListener(sensorListener):

  def __init__(self, feed_sensor, feed_gadget_modify, client: Adafruit):
    super().__init__(feed_sensor, feed_gadget_modify, client)
  
  def update(self, data):
    if get_mode("light") != "automatic":
      return
    
    if int(data) < 30:
      light_power = 100 - int(data)
      self._controller.add_command(lightingModify(self._client, self._feed_gadget_modify, light_power))
      self._controller.excute_command()
      
    elif int(data) > 60:
      light_power = 0
      self._controller.add_command(lightingModify(self._client, self._feed_gadget_modify, light_power))
      self._controller.excute_command()


