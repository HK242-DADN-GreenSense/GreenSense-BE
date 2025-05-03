from pymongo.collection import Collection 
from typing import TypedDict
from datetime import datetime
from .. import db

class Scheduler_Job(TypedDict):
    job_id: str
    device_id: str
    action: str
    action_options: dict
    trigger: str
    trigger_options: dict
    
scheduler_job_collection : Collection[Scheduler_Job] = db['scheduler_job']