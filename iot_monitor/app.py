import logging
import asyncio
# from iot import sensor
from .iot_config import LOG_FILE, DEPLOYMENT_ENV, LOG_FORMAT

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format=LOG_FORMAT, filemode='w')
logger = logging.getLogger(__name__)

def run():
    from .iot.sensor import Sensor
    iotSensor = Sensor(DEPLOYMENT_ENV)
    iotSensor.start_receive()

if __name__ == '__main__':
    run()