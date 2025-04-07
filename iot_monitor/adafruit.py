
from Adafruit_IO import MQTTClient
from typing import List, Tuple

class Adafruit:
    __feeds_gadgets_list: List[str]
    # __feed_list_iot: List[str]

    __client: MQTTClient
    __message_queue: List[Tuple]

    def __init__(self, username, io_key, feed_iot_gadget):

      self.__client = MQTTClient(username, io_key)
      self.__message_queue = list()
      self.__feeds_gadgets_list = feed_iot_gadget

      def connected(client):
        feed_sensor = list(map(lambda x: x[0],  self.__feeds_gadgets_list))
        for feed_id in feed_sensor:
          self.__client.subscribe(feed_id)  # Đăng ký nhận dữ liệu từ feed
        print("✅ Connected to Adafruit IO!")  # Hiển thị khi kết nối thành công
  
          
      # Hàm callback khi bị mất kết nối
      def disconnected(client):
        print("❌ Disconnected from Adafruit IO!")

      # Hàm callback khi nhận được dữ liệu từ feed
      def message(client, feed_id, payload):
        print(f"📩 Received data: {payload} from {feed_id}")
        self.__message_queue.append((feed_id, payload)) 
      
      # Gán các hàm callback
      self.__client.on_connect = connected
      self.__client.on_disconnect = disconnected
      self.__client.on_message = message
  
    def getFeeds(self):
      return self.__feeds_gadgets_list
    
    def start(self):
      self.__client.connect()
      self.__client.loop_background()

    def disconnect(self):
      self.__client.disconnect()

    # update data to feed
    def update_data(self, feed_id, data):
      self.__client.publish(feed_id, data)
      
    def get_message_queue(self):
      return self.__message_queue

    def pop_message_queue(self):
      self.__message_queue.pop(0)