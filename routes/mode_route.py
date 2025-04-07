from flask import Blueprint
from ..controllers.iot_mode_controller import *

IOT_mode = Blueprint(name="IOT_mode", import_name=__name__)

@IOT_mode.route('/pump/automation')
def pump_automation():
    return ctl_pump_automation()

@IOT_mode.route('/pump/manual')
def pump_manual():
    return ctl_pump_manual()

@IOT_mode.route('/fan/automation')
def fan_automation():
    return ctl_fan_automation()

@IOT_mode.route('/fan/manual')
def fan_manual():
    return ctl_fan_manual()

@IOT_mode.route('/servo/automation')
def servo_automation():
    return ctl_servo_automation()

@IOT_mode.route('/servo/manual')
def servo_manual():
    return ctl_servo_manual()

@IOT_mode.route('/light/automation')
def light_automation():
    return ctl_light_automation()

@IOT_mode.route('/light/manual')
def light_manual():
    return ctl_light_manual()

