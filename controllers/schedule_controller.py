from .. import scheduder
from .adafruit_controller import *
from time import sleep
    
def ctl_pump_schedule_control():
    ctl_adafruit_pump(status='on')
    sleep(20)
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