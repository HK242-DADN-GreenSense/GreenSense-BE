from ..collection.schedule_job_collection import scheduler_job_collection

def model_schedule_get_job(device_id: str | None = None):
    filter = None
    
    if device_id:
        filter = {
            "device_id": device_id
        }

    return scheduler_job_collection.find(filter=filter).to_list()

def model_schedule_insert_job(job_id, device_id, action, action_options, trigger, trigger_options):
    try: 
        document = {
            "job_id": job_id,
            "device_id": device_id,
            "action": action,
            "action_options": action_options,
            "trigger": trigger,
            "trigger_options": trigger_options
        }
        
        obj_id = scheduler_job_collection.insert_one(document).inserted_id
        
        return obj_id
        
    except Exception as e:
        print(f"Error in model_schedule_insert_job: {e}")
        return None

def model_schedule_delete_all_job():
    try:
        scheduler_job_collection.delete_many({})
        return True
    except Exception as e:
        print(f'Error in model_schedule_delete_all_job: {e}')
        return False