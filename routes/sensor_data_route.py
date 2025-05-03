from flask import Blueprint, request
import datetime
from ..controllers.sensor_data_controller import *

sensor_data = Blueprint("sensor_data", __name__)

@sensor_data.route('/api/sensor_data/humid', methods=['GET'])
def route_get_humid_data():
    _year = int(request.args.get('year'))
    _month = int(request.args.get('month'))
    _date = int(request.args.get('date'))
    
    # date = datetime.date.today()
    
    if _year and _month and _date:
        try:
            date = datetime(_year, _month, _date).date()
        except ValueError:
            print("Invalid date input")
            return {
                'success': False,
                'message': "Invalid date input"
            }, 400

    return ctl_sensor_data_get_humid_data(date)

@sensor_data.route('/api/sensor_data/light', methods=['GET'])
def route_get_light_data():
    _year = int(request.args.get('year'))
    _month = int(request.args.get('month'))
    _date = int(request.args.get('date'))
    
    # date = datetime.date.today()
    
    if _year and _month and _date:
        try:
            date = datetime(_year, _month, _date).date()
        except ValueError:
            print("Invalid date input")
            return {
                'success': False,
                'message': "Invalid date input"
            }, 400

    return ctl_sensor_data_get_light_data(date)

@sensor_data.route('/api/sensor_data/temperature', methods=['GET'])
def route_get_temperature_data():
    _year = int(request.args.get('year'))
    _month = int(request.args.get('month'))
    _date = int(request.args.get('date'))
    
    # date = datetime.date.today()
    
    if _year and _month and _date:
        try:
            date = datetime(_year, _month, _date).date()
        except ValueError:
            print("Invalid date input")
            return {
                'success': False,
                'message': "Invalid date input"
            }, 400

    return ctl_sensor_data_get_temperature_data(date)