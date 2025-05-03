from flask import Blueprint, request
from ..controllers.iot_mode_controller import *

IOT_mode = Blueprint(name="IOT_mode", import_name=__name__)

@IOT_mode.route('/api/mode/get', methods=["GET"])
def route_mode_get():
    return ctl_mode_get()

@IOT_mode.route('/api/mode/pump/automation', methods=["POST"])
def pump_automation():
    data = request.get_json()
    
    if not data or "automatic_options" not in data:
        return {
            'success': False,
            'message': "Empty request body or missing 'automatic_options' parameter"    
        }, 400
    
    automatic_options = data["automatic_options"]
    
    # Validate automatic_options
    # Check if "threshold" and "duration" is in automatic_options
    if "threshold" not in automatic_options:
        return {
            'success': False,
            'message': "'automatic_options' parameter doesn't contain 'threshold' value"    
        }, 400
        
    if "duration" not in automatic_options:
        return {
            'success': False,
            'message': "'automatic_options' parameter doesn't contain 'duration' value"    
        }, 400

    return ctl_pump_automation(automatic_options)

@IOT_mode.route('/api/mode/pump/manual', methods=["POST"])
def pump_manual():
    return ctl_pump_manual()

@IOT_mode.route('/api/mode/servo/automation', methods=["POST"])
def servo_automation():
    data = request.get_json()
    
    if not data or "automatic_options" not in data:
        return {
            'success': False,
            'message': "Empty request body or missing 'automatic_options' parameter"    
        }, 400
    
    automatic_options = data["automatic_options"]
    # Validate automatic_options
    if "temperatures" not in automatic_options:
        return {
            'success': False,
            'message': "'automatic_options' parameter doesn't contain 'temperatures' value"    
        }, 400
        
    if "angles" not in automatic_options:
        return {
            'success': False,
            'message': "'automatic_options' parameter doesn't contain 'angles' value"    
        }, 400
    return ctl_servo_automation(automatic_options)

@IOT_mode.route('/api/mode/servo/manual', methods=["POST"])
def servo_manual():
    return ctl_servo_manual()

@IOT_mode.route('/api/mode/light/automation', methods=["POST"])
def light_automation():
    data = request.get_json()

    if not data or "automatic_options" not in data:
        return {
            'success': False,
            'message': "Empty request body or missing 'automatic_options' parameter"    
        }, 400

    automatic_options = data["automatic_options"]
    
    # Validate automatic_options
    if "lights" not in automatic_options:
        return {
            'success': False,
            'message': "'automatic_options' parameter doesn't contain 'lights' value"    
        }, 400
        
    if "intensities" not in automatic_options:
        return {
            'success': False,
            'message': "'automatic_options' parameter doesn't contain 'intensities' value"    
        }, 400
    return ctl_light_automation(automatic_options)

@IOT_mode.route('/api/mode/light/manual', methods=["POST"])
def light_manual():
    return ctl_light_manual()

