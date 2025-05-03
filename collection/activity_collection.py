from pymongo.collection import Collection 
from typing import TypedDict
from datetime import datetime
from .. import db
# from ..app import db

class Activity(TypedDict):
    time: datetime
    data: int
    activity_type: str

activity_collection: Collection[Activity] = db['activity']
# command_collection: Collection[Command] = db["command"]
