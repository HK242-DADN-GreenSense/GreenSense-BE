import time
import os
from ..config import LOG_DIR

DEPLOYMENT_ENV = {
  "ADAFRUIT_IO_KEY": 'aio_CNzr15m68WWUQ8iAb8RarG68ffFL',
  "ADAFRUIT_IO_USERNAME": 'trananhkhoitv',
  "IOT_GADGET": [
    ('humid', 'pump'),
    ('temperature', 'servo'),
    ('light-sensor', 'light'),
    ('pump', ""),
    ('servo', ""),
    ('light', "")
  ]
}

LOG_FORMAT = '%(asctime)s %(message)s'
LOG_FILE_NAME = f"iot_monitor_{time.strftime("%Y%m%d-%H%M%S", time.localtime())}.log"
LOG_FILE = os.path.join(LOG_DIR, LOG_FILE_NAME)
