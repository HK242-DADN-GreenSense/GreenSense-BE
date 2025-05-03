from pymongo.collection import Collection 
from typing import TypedDict
from datetime import datetime
from .. import db

class Light(TypedDict):
    time: datetime
    data: int

light_collection: Collection[Light] = db['light']
# command_collection: Collection[Command] = db["command"]
