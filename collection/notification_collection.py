from pymongo import MongoClient
from ..config import MONGO_URI
from .. import db

notification_collection = db['notifications']