import os

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
LOG_DIR = os.path.join(WORKING_DIR, 'var', 'log')
IOT_ENV = os.path.join(WORKING_DIR, "iot_env.json")

""" Config for GreenSense backend package """
# MONGO_URI               = "mongodb+srv://tnpht7404:aKrKJMMRyXyw345G@cluster0.c5yym.mongodb.net/"
MONGO_URI                 = "mongodb+srv://greensense_dev:641abbPRVszJJrbT@cluster0.yvtnh.mongodb.net"
# ADAFRUIT_AIO_USERNAME   = "hieuduongk22bk"
# ADAFRUIT_AIO_KEY        = "aio_CgOe77qUN0Gdvfnb0sqMCTXErAdS"


ADAFRUIT_AIO_USERNAME = "trananhkhoitv"
ADAFRUIT_AIO_KEY      = "aio_CNzr15m68WWUQ8iAb8RarG68ffFL"
