from flask import Blueprint
from ..controllers.adafruit_controller import *
ada_fruit = Blueprint('ada_fruit', __name__)

@ada_fruit.route('/apa_fruit/send')
def route_ada_fruit_send():
    return ctl_feed_testing()