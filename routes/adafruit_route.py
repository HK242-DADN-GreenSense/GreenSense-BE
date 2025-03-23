from flask import Blueprint, request, jsonify
from ..controllers.adafruit_controller import *
from flasgger import swag_from

ada_fruit = Blueprint('ada_fruit', __name__)

# @ada_fruit.route('/api/adafruit/pump/on')
# def route_adafruit_pump_on():
#     return ctl_adafruit_pump(on=True)

# @ada_fruit.route('/api/adafruit/pump/off')
# def route_adafruit_pump_off():
#     return ctl_adafruit_pump(on=False)
  
  
@ada_fruit.route('/api/adafruit/pump/', methods=['POST'])
def route_adafruit_pump():
    try:
        data = request.get_json()
        
        if not data or 'status' not in data:
            return jsonify({
                'success': False,
                'message': 'Missing status parameter'
            }), 400
            
        status = data['status']
        return jsonify(ctl_adafruit_pump(status))
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500
  
    
@ada_fruit.route('/apa_fruit/send')
def route_ada_fruit_send():
    """
    Test Adafruit IO connection
    ---
    responses:
      200:
        description: Successfully tested Adafruit IO connection
        schema:
          properties:
            success:
              type: boolean
              example: true
    """
    return ctl_feed_testing()

@ada_fruit.route('/servo', methods=['POST'])
def servo_control():
    """
    Control servo position
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - angle
          properties:
            angle:
              type: number
              minimum: 0
              maximum: 180
              description: Servo angle between 0 and 180 degrees
              example: 90
    responses:
      200:
        description: Servo angle set successfully
        schema:
          properties:
            success:
              type: boolean
              example: true
            angle:
              type: number
              example: 90
      400:
        description: Invalid request parameters
        schema:
          properties:
            success:
              type: boolean
              example: false
            message:
              type: string
              example: "Angle must be between 0 and 180"
      500:
        description: Server error
        schema:
          properties:
            success:
              type: boolean
              example: false
            message:
              type: string
              example: "Error message"
    """
    try:
        data = request.get_json()
        
        if not data or 'angle' not in data:
            return jsonify({
                'success': False,
                'message': 'Missing angle parameter'
            }), 400
            
        angle = float(data['angle'])
        return jsonify(ctl_servo(angle))
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500