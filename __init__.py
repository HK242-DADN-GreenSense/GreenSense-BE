""" GreenSense backend package """

from flask                              import Flask, jsonify
from flask_cors                         import CORS, cross_origin
from flask_pymongo                      import MongoClient
from Adafruit_IO                        import Client, RequestError, Feed
from pymongo.database                   import Database
from flasgger                           import Swagger
from apscheduler.schedulers.background  import BackgroundScheduler 
from flask_socketio                     import SocketIO
from .config                            import *

app = Flask(__name__)
cors = CORS(app)
# Initialize SocketIO after creating your Flask app
socketio = SocketIO(app, cors_allowed_origins="*")

# Configure Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}
swagger = Swagger(app, config=swagger_config)

client : MongoClient = MongoClient(MONGO_URI)
db : Database = client.greensense
aio = Client(username=ADAFRUIT_AIO_USERNAME, key=ADAFRUIT_AIO_KEY)
scheduder = BackgroundScheduler() 
scheduder.start()

from .routes.command_route      import command      as command_blueprint
from .routes.adafruit_route     import ada_fruit    as adafruit_blueprint
from .routes.iot_mode_route     import IOT_mode     as iot_mode_blueprint
from .routes.schedule_route     import schedule_blueprint
from .routes.app_route          import app_route     as app_blueprint
from .routes.notification_route import notification_route as notification_blueprint
from .routes.sensor_data_route  import sensor_data as sensor_data_blueprint

app.register_blueprint(command_blueprint)
app.register_blueprint(adafruit_blueprint)
app.register_blueprint(iot_mode_blueprint)
app.register_blueprint(schedule_blueprint)
app.register_blueprint(app_blueprint, url_prefix='')  # Explicitly set empty prefix
app.register_blueprint(notification_blueprint, url_prefix='')
app.register_blueprint(sensor_data_blueprint)

# Import and initialize your socketio service
from .services.socketio_service import initialize_socketio
initialize_socketio(socketio)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
