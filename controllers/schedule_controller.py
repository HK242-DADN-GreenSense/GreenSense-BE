from .. import scheduder
from .adafruit_controller import *
from ..models.schedule_model import *
from ..common.json_utility import *
from time import sleep
from flask import jsonify

def ctl_job_fetch(device_id: str | None = None):
    try:
        job_list = model_schedule_get_job(device_id)

        print(job_list, type(job_list))
            
        return parse_json({
            "success": True,
            "message": "Fetch job successfully",
            "job_list": job_list
        }), 200
        
    except Exception as e:
        print(f"Error in ctl_job_fetch: {e}")
        return {
            'success': False,
            'message': str(e)
        }, 500

def ctl_job_load():
    job_list = model_schedule_get_job()
    
    if not model_schedule_delete_all_job():
        return {
            "success": False,
            "message": "Reload job failed"
        }, 500
    
    for job in job_list:
        _, code = ctl_job_add({
            "device_id": job["device_id"],
            "trigger": job["trigger"],
            "trigger_options": job["trigger_options"],
            "action": job["action"],
            "action_options": job["action_options"]
        })
        
        if code != 200:
            scheduder.remove_all_jobs()
            
            if not model_schedule_delete_all_job():
                return {
                    "success": False,
                    "message": "Reload job failed"
                }, 500
                
            return {
                "success": False,
                "message": "Reload job failed"
            }, 500
        
    return {
        "success": True,
        "message": "Load old job successfully"
    }, 200

def ctl_job_add(data):
    device_id = data["device_id"]
    trigger = data["trigger"]
    trigger_options = data["trigger_options"]
    action = data["action"]
    action_options = data["action_options"]
    if (device_id == 'pump'):
        return ctl_schedule_pump_add_job(trigger, trigger_options, action, action_options)
    elif (device_id == 'light'):
        return ctl_schedule_light_add_job(trigger, trigger_options, action, action_options)
    elif (device_id == 'servo'):
        return ctl_schedule_servo_add_job(trigger, trigger_options, action, action_options)
    else:
        return {
            'success': False,
            'message': "Unknown device id"
        }, 400

def ctl_job_remove(job_id):
    try:
        scheduler_job_collection.find_one_and_delete({"job_id": job_id})
        
        scheduder.remove_job(job_id)
        
        return {
            'success': True,
            'message': f"Remove job with job_id-{job_id} successfully"
        }, 200
        
    except Exception as e:
        print(f"Error in ctl_job_remove: {e}")
        return {
            'success': False,
            'message': str(e)
        }, 500

# def ctl_job_modify(data):
#     job_id = data["job_id"]
#     trigger = data["trigger"]
#     trigger_options = data["trigger_options"]
    
#     modified_job = scheduder.modify_job(job_id=job_id, trigger=trigger, **trigger_options)

def ctl_schedule_pump_add_job(trigger, trigger_options, action, action_options):
    if "duration" not in action_options :
        return {
            'success': False,
            'message': "Invalid action option"
        }, 400
        
    try:
        duration = int(action_options['duration']) 

        added_job = scheduder.add_job(func=ctl_adafruit_pump_duration, args=[duration], trigger=trigger, **trigger_options)

        model_schedule_insert_job(job_id=added_job.id, device_id="pump", trigger=trigger, trigger_options=trigger_options, action=action, action_options=action_options)
        
        return {
            "success": True,
            "message": "Added job successfully",
            "job_id": added_job.id
        }, 200
    except Exception as e:
        print(f'Error in ctl_schedule_pump_add_job: {e}')
        return {
            'success': False,
            'message': str(e)
        }, 500
        
def ctl_schedule_light_add_job(trigger, trigger_options, action, action_options):
    if "intensity" not in action_options :
        return {
            'success': False,
            'message': "Invalid action option"
        }, 400
        
    try:
        intensity = int(action_options['intensity']) 

        added_job = scheduder.add_job(func=ctl_adafruit_light, args=[intensity], trigger=trigger, **trigger_options)

        model_schedule_insert_job(job_id=added_job.id, device_id="light", trigger=trigger, trigger_options=trigger_options, action=action, action_options=action_options)
        
        return {
            "success": True,
            "message": "Added job successfully"
        }, 200
    except Exception as e:
        print(f'Error in ctl_schedule_light_add_job: {e}')
        return {
            'success': False,
            'message': str(e)
        }, 500

def ctl_schedule_servo_add_job(trigger, trigger_options, action, action_options):
    if "angle" not in action_options :
        return {
            'success': False,
            'message': "Invalid action option"
        }, 400
        
    try:
        angle = int(action_options['angle']) 
        
        added_job = scheduder.add_job(func=ctl_adafruit_servo, args=[angle], trigger=trigger, **trigger_options)

        model_schedule_insert_job(job_id=added_job.id, device_id="servo", trigger=trigger, trigger_options=trigger_options, action=action, action_options=action_options)
        
        return {
            "success": True,
            "message": "Added job successfully"
        }, 200
    except Exception as e:
        print(f'Error in ctl_schedule_servo_add_job: {e}')
        return {
            'success': False,
            'message': str(e)
        }, 500

def ctl_pump_schedule_control():
    ctl_adafruit_pump(status='on')
    sleep(10)
    ctl_adafruit_pump(status='off')
    
def ctl_pump_interval_schedule(time_unit: str, amount: int):
    if time_unit not in ['second', 'minute', 'hour', 'day']:
        return {
            'success': False,
            'message': "time_unit must be 'second', 'minute', 'hour' or 'day'"
        }, 400
    
    if time_unit == 'second':
        job = scheduder.add_job(func=ctl_pump_schedule_control, trigger='interval', seconds=amount)
    elif time_unit == 'minute':
        job = scheduder.add_job(func=ctl_pump_schedule_control, trigger='interval', minutes=amount)
    elif time_unit == 'hour':
        job = scheduder.add_job(func=ctl_pump_schedule_control, trigger='interval', hours=amount)
    elif time_unit == 'day':
        job = scheduder.add_job(func=ctl_pump_schedule_control, trigger='interval', days=amount)
    
    return {
        'success': True,
        'message': "Add job succesfully",
        'job_id': job.id
    }, 200
    
def ctl_pump_remove_job(job_id: str):
    try:
        scheduder.remove_job(job_id=job_id)
    
        return {
            'success': True,
            'message': 'Remove job successfully'
        }, 200
    except Exception as e:
        print(f'Error in ctl_pump_remove_job: {e}')
        return {
            'success': False,
            'message': f'Error in ctl_pump_remove_job: {e}'
        }, 400