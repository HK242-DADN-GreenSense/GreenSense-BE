from pymongo.collection import Collection 
from typing import TypedDict
from datetime import datetime
from .. import db

class Humid(TypedDict):
    time: datetime
    data: int

humid_collection: Collection[Humid] = db['humid']
# command_collection: Collection[Command] = db["command"]
