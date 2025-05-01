from .. import app
from flask import jsonify
from datetime import datetime
from ..services.socketio_service import emit_sensor_data
from flask import Blueprint

app_route = Blueprint('app_route', __name__) 

@app_route.route('/')  # Add a root route
def root():
    """Root endpoint for basic testing"""
    return jsonify({
        'success': True,
        'message': 'Root endpoint is working'
    }), 200

@app_route.route('/status')
def hello_world():
    """ Testing if flask app is running """
    return jsonify({
        'success': True,
        'message': 'Flask app is working'
    }), 200

@app_route.route('/test-emit')
def test_emit():
    """Test endpoint to emit a socket event for temperature."""
    emit_sensor_data('temperature', 25.5, datetime.utcnow())
    return jsonify({
        'success': True,
        'message': 'Socket event emitted for temperature'
    }), 200