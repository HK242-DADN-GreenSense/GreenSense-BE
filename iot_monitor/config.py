DEPLOYMENT_ENV = {
  "ADAFRUIT_IO_KEY": 'aio_CNzr15m68WWUQ8iAb8RarG68ffFL',
  "ADAFRUIT_IO_USERNAME": 'trananhkhoitv',
  "IOT_GADGET": [
    ('humid', 'pump'),
    ('temperature', 'servo'),
    ('light-sensor', 'light')
  ]
}

LOG_FORMAT = '%(asctime)s %(message)s'
LOG_FILE = "/home/khoitrananh/working/CO3109/greensense_be/iot_monitor/iot_monitor.log"

MONGO_URI = "mongodb+srv://greensense_dev:641abbPRVszJJrbT@cluster0.yvtnh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"