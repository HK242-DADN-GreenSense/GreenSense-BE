from pymongo.collection import Collection 
from typing import TypedDict
from datetime import datetime

from ..app import db

class Temperature(TypedDict):
    time: datetime
    data: int

temperature_collection: Collection[Temperature] = db['temperature']
# command_collection: Collection[Command] = db["command"]
