
from abc import ABC, abstractmethod
from .adafruit import Adafruit
from ..app import logger
# from .. import logger
import time

class Command(ABC):
    _client: Adafruit
    _feed_name: str
    def __init__(self, system, feed_name, data):
        self._client = system
        self._feed_name = feed_name
        self._data = data

    @abstractmethod
    def execute(self, data):
        pass

class waterModify(Command):

    def __init__(self, wateringSystem, feed_name, data):
        super().__init__(wateringSystem, feed_name, data)

    def execute(self):
        # print(self._feed_name,  self._data)
        self._client.update_data(self._feed_name, self._data)
        if (self._data == 0):
            logger.info(msg="Turning pump off")
        elif (self._data == 1):
            logger.info(msg="Turning pump on")
        
class lightingModify(Command):
    def __init__(self, lightingSystem, feed_name, data):
        super().__init__(lightingSystem, feed_name, data)

    def execute(self):
        self._client.update_data(self._feed_name, self._data)
        if (self._data == 0):
            logger.info(msg="Turning off the light")
        else:
            logger.info(msg="Turning on the light")
            

class temperatureModify(Command):
    def __init__(self, temperatureSystem, feed_name, data):
        super().__init__(temperatureSystem, feed_name, data)

    def execute(self):
        self._client.update_data(self._feed_name, self._data)
        if (self._data == 0): 
            logger.info(msg="Closing cover")
        else:
            logger.info(msg="Opening cover")

class smartFarmController:
    def __init__(self):
        self.commands = []

    def add_command(self, command: Command):
        self.commands.append(command)

    def excute_command(self):
        # time.sleep(15)
        if len(self.commands) != 0:
            # TẠO RA BẢN SAO TRÁNH GÂY XUNG ĐỘT TẠI THỜI ĐIỂM LẶP VÌ SẼ CÓ TÌNH HUỐNG APPEND COMMAND KHÁC VÀO
            for command in self.commands[:]:
                command.execute()
                self.commands.pop(0)

