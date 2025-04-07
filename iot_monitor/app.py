import logging
from sensor import Sensor
from config import LOG_FILE, DEPLOYMENT_ENV

logger = logging.getLogger(__name__)

if __name__ == '__main__':
  logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)
  iotSensor = Sensor(DEPLOYMENT_ENV)
  iotSensor.start_receive()