from flask import Flask, jsonify
from flask_pymongo import MongoClient

from .config import *

app = Flask(__name__)

client = MongoClient(MONGO_URI)
db = client.GreenSenseDB

@app.route('/')
def helloWorld():
    return jsonify({
        'success': True,
        'message': 'Flask app is working'
    }), 200