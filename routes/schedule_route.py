from flask import Blueprint
from ..controllers.schedule_controller import ctl_pump_interval_schedule, ctl_pump_remove_job

schedule_blueprint = Blueprint("scheduler", __name__)

@schedule_blueprint.route('/api/pump/schedule/add/interval/<time_unit>/<amount>')
def route_sched_pump_add_job(time_unit: str, amount: int):
    return ctl_pump_interval_schedule(time_unit, int(amount))

@schedule_blueprint.route('/api/pump/schedule/remove/<job_id>')
def route_sched_pump_remove_job(job_id):
    return ctl_pump_remove_job(job_id)
    