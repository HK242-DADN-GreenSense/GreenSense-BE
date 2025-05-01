import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to server")

@sio.on('sensor_temperature')
def on_temperature(data):
    print("Temperature data:", data)

sio.connect('http://localhost:5000')
sio.wait()