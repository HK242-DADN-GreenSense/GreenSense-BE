import logging
# from iot import sensor
from .config import LOG_FILE, DEPLOYMENT_ENV, LOG_FORMAT, MONGO_URI
from pymongo import MongoClient

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format=LOG_FORMAT, filemode='w')
logger = logging.getLogger(__name__)

client = MongoClient(MONGO_URI)
db = client['greensense']

def run():
    from .iot.sensor import Sensor
    iotSensor = Sensor(DEPLOYMENT_ENV)
    iotSensor.start_receive()

if __name__ == '__main__':
    run()