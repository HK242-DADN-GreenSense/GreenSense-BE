from flask import Blueprint
from ..controllers.adafruit_controller import *
ada_fruit = Blueprint('ada_fruit', __name__)

@ada_fruit.route('/apa_fruit/fan/<speed>')
def route_ada_fruit_send(spped):
    return ctl_feed_testing(spped)

@ada_fruit.route('/api/adafruit/pump/on')
def route_adafruit_pump_on():
    return ctl_adafruit_pump(on=True)

@ada_fruit.route('/api/adafruit/pump/off')
def route_adafruit_pump_off():
    return ctl_adafruit_pump(on=False)