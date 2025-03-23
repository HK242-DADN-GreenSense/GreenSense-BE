""" GreenSense backend package """

from flask import Flask, jsonify
from flask_pymongo import MongoClient
from Adafruit_IO import Client, RequestError, Feed
from pymongo.database import Database
from flasgger import Swagger

from .config import *

app = Flask(__name__)

# Configure Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

swagger = Swagger(app, config=swagger_config)

client : MongoClient = MongoClient(MONGO_URI)
db : Database = client.GreenSenseDB
aio = Client(username=ADAFRUIT_AIO_USERNAME, key=ADAFRUIT_AIO_KEY)

from .routes.command_route import command as command_blueprint
from .routes.adafruit_route import ada_fruit as adafruit_blueprint
from .routes.app_route import *

app.register_blueprint(command_blueprint)
app.register_blueprint(adafruit_blueprint)
