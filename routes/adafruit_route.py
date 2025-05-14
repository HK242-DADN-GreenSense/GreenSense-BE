from flask import Blueprint, request, jsonify
from ..controllers.adafruit_controller import *
from flasgger import swag_from

ada_fruit = Blueprint('ada_fruit', __name__)

@ada_fruit.route('/api/adafruit/pump', methods=['POST'])
def route_adafruit_pump():
	try:
		data = request.get_json()
		
		if not data or 'status' not in data:
			return jsonify({
				'success': False,
				'message': 'Missing status parameter'
			}), 400
			
		status = data['status']
		return ctl_adafruit_pump(status)
		
	except Exception as e:
		return jsonify({
			'success': False,
			'message': str(e)
		}), 500

@ada_fruit.route('/api/adafruit/pump/on', methods=["POST"])
def route_adafruit_pump_duration():
	try:
		data = request.get_json()
		
		if not data or "duration" not in data:
			return jsonify({
				"success": False,
				"message": "Missing duration parameter"
			}), 400
		
		duration = int(data['duration'])
		return ctl_adafruit_pump_duration(duration)
	except Exception as e:
		return jsonify({
			"success": False,
			"message": str(e)
			}), 500  

@ada_fruit.route('/api/adafruit/servo', methods=['POST'])
def route_adafruit_servo():
	try:
		data = request.get_json()
		
		if not data or 'angle' not in data:
			return jsonify({
				'success': False,
				'message': 'Missing angle parameter'
			}), 400
			
		angle = float(data['angle'])
		return ctl_adafruit_servo(angle)
		
	except Exception as e:
		return jsonify({
			'success': False,
			'message': str(e)
		}), 500

@ada_fruit.route('/api/adafruit/fan', methods=['POST'])
def route_adafruit_fan():
	try:
		data = request.get_json()
		
		if not data or 'speed' not in data:
			return jsonify({
				'success': False,
				'message': 'Missing speed parameter'
			}), 400
			
		speed = int(data['speed'])
		return ctl_adafruit_fan(speed)
		
	except Exception as e:
		return jsonify({
			'success': False,
			'message': str(e)
		}), 500

@ada_fruit.route('/api/adafruit/light', methods=['POST'])
def route_adafruit_light():
	try:
		data = request.get_json()
		
		if not data or 'intensity' not in data:
			return jsonify({
				'success': False,
				'message': 'Missing intensity parameter'
			}), 400
			
		intensity = int(data['intensity'])

		return ctl_adafruit_light(intensity)
		
	except Exception as e:
		return jsonify({
			'success': False,
			'message': str(e)
		}), 500