from pymongo.collection import Collection 
from typing import TypedDict

from .. import db

class Command(TypedDict):
    name: str
    type: int

command_collection: Collection[Command] = db["command"]
