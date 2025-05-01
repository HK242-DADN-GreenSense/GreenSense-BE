from flask_socketio import SocketIO

_socketio = None

def initialize_socketio(socketio_instance):
    """Initialize the socketio service with the Flask-SocketIO instance"""
    global _socketio
    _socketio = socketio_instance

def emit_sensor_data(sensor_type, value, timestamp):
    """Emit sensor data to connected clients"""
    if _socketio:
        print(f"Emitting {sensor_type} data: {value}")
        _socketio.emit(f'sensor_{sensor_type}', {
            'value': value,
            'timestamp': timestamp.isoformat() if hasattr(timestamp, 'isoformat') else str(timestamp)
        })