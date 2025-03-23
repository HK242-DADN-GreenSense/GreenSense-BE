from flask import Blueprint
from ..controllers.adafruit_controller import *
ada_fruit = Blueprint('ada_fruit', __name__)

@ada_fruit.route('/api/ada_fruit/fan/<speed>', methods = ['GET'])
def route_ada_fruit_send_fan(speed):
    return send_fan_req(speed)