from datetime import date, datetime

from ..collection.humid_collection import humid_collection
from ..collection.light_collection import light_collection
from ..collection.temperature_collection import temperature_collection

def model_get_humid_data(date : date):
    try:
        start = datetime.combine(date, datetime.min.time())
        end = datetime.combine(date, datetime.max.time())
        
        humid_data = humid_collection.find({"time": {"$gte": start, "$lte": end}}).to_list()
        
        return humid_data, True
    except Exception as e:
        print(f'Error in model_get_humid_data: {e}')
        return [], False
    

def model_get_light_data(date):
    try:
        start = datetime.combine(date, datetime.min.time())
        end = datetime.combine(date, datetime.max.time())
        
        light_data = light_collection.find({"time": {"$gte": start, "$lte": end}}).to_list()
        
        return light_data, True
    except Exception as e:
        print(f'Error in model_get_light_data: {e}')
        return [], False

def model_get_temperature_data(date):
    try:
        start = datetime.combine(date, datetime.min.time())
        end = datetime.combine(date, datetime.max.time())
        
        temperature_data = temperature_collection.find({"time": {"$gte": start, "$lte": end}}).to_list()
        
        return temperature_data, True
    except Exception as e:
        print(f'Error in model_get_temperature_data: {e}')
        return [], False