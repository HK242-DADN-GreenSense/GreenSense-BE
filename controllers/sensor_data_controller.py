import datetime

from ..common.json_utility import parse_json
from ..models.sensor_data_model import *

def ctl_sensor_data_get_humid_data(date):
    data, success = model_get_humid_data(date)
    
    if not success:
        return {
            'success': False,
            'message': "Error while fetching data from MongoDB"
        }, 500
        
    return parse_json({
        'success': True,
        'message': "Fetch humid data successfully",
        'data': data
    }), 200
    
def ctl_sensor_data_get_light_data(date):
    data, success = model_get_light_data(date)
    
    if not success:
        return {
            'success': False,
            'message': "Error while fetching data from MongoDB"
        }, 500
        
    return parse_json({
        'success': True,
        'message': "Fetch light data successfully",
        'data': data
    }), 200
    
def ctl_sensor_data_get_temperature_data(date):
    data, success = model_get_temperature_data(date)
    
    if not success:
        return {
            'success': False,
            'message': "Error while fetching data from MongoDB"
        }, 500
        
    return parse_json({
        'success': True,
        'message': "Fetch temperature data successfully",
        'data': data
    }), 200