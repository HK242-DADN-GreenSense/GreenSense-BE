""" GreenSense backend package """

from flask import Flask, jsonify
from flask_pymongo import MongoClient
from pymongo.database import Database

from .config import *

app = Flask(__name__)

client : MongoClient = MongoClient(MONGO_URI)
db : Database = client.GreenSenseDB

from .routes.command_route import command as command_blueprint

app.register_blueprint(command_blueprint)
