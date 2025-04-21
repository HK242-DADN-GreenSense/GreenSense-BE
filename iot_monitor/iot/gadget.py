
from Adafruit_IO import MQTTClient
from typing import List, Tuple
from ..app import logger
from ..collection.activity_collection import activity_collection
from time import sleep, time
ADAFRUIT_IO_KEY = 'aio_CNzr15m68WWUQ8iAb8RarG68ffFL'
ADAFRUIT_IO_USERNAME = 'trananhkhoitv'

class Gadget_Adafruit:
	__client: MQTTClient

	def __init__(self, username, io_key):

		self.__client = MQTTClient(username, io_key)
		
		def connected(client):
			feed_sensor = ["pump", "fan", "servo", "light"]
			for feed_id in feed_sensor:
				self.__client.subscribe(feed_id)  # Đăng ký nhận dữ liệu từ feed
			logger.info(msg="✅ Connected to Adafruit IO!") # Hiển thị khi kết nối thành công

				
		# Hàm callback khi bị mất kết nối
		def disconnected(client):
			logger.info(msg="❌ Disconnected from Adafruit IO!") # Hiển thị khi kết nối thành công

		# Hàm callback khi nhận được dữ liệu từ feed
		def message(client, feed_id, payload):
			logger.info(msg=f"📩 Received data: {payload} from {feed_id}") # Hiển thị khi kết nối thành công
			document = {
				"time": time(),
				"data": payload,
				"type": feed_id,
			}
			activity_collection.insert_one(document=document)
			logger.info(msg=f"Inserted one document into MongoDB on {feed_id} collection") # Hiển thị khi kết nối thành công
			
			# Gán các hàm callback
		self.__client.on_connect = connected
		self.__client.on_disconnect = disconnected
		self.__client.on_message = message

	def start(self):
		self.__client.connect()
		self.__client.loop_background()

	def disconnect(self):
		self.__client.disconnect()
  
def run_gadget_listener():
    gadget_listener = Gadget_Adafruit(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
    gadget_listener.start()
    while True:
        sleep(10)