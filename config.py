import os

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
LOG_DIR = os.path.join(WORKING_DIR, 'var', 'log')
IOT_ENV = os.path.join(WORKING_DIR, "iot_env.json")

""" Config for GreenSense backend package """
MONGO_URI                 = "MONGO_URI"
ADAFRUIT_AIO_USERNAME   = "ADAFRUIT_AIO_USERNAME"
ADAFRUIT_AIO_KEY        = "ADAFRUIT_AIO_KEY"
