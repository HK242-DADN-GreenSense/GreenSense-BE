from flask import Blueprint, request, jsonify
from ..controllers.schedule_controller import *
from ..common.validate_job_trigger import *

schedule_blueprint = Blueprint("scheduler", __name__)

@schedule_blueprint.route("/api/job/get", methods=["GET"])
def route_sched_get_job():
    device_id = request.args.get("device_id")
    return ctl_job_fetch(device_id)

@schedule_blueprint.route("/api/job/load", methods=["POST"])
def route_sched_load_job():
    return ctl_job_load()

@schedule_blueprint.route("/api/job/add", methods=["POST"])
def route_sched_add_job():
    required_fields = ["device_id", "trigger", "trigger_options", "action", "action_options"]
    try: 
        data = request.get_json()
        
        if not data:
            return jsonify({
				'success': False,
				'message': 'Empty body'
			}), 400
        
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'success': False,
                    'message': f'Missing "{field}" parameter'
                }), 400
                
        if data['trigger'] == "interval" and not validate_interval_job_option(data['trigger_options']):
            return jsonify({
                'success': False,
                'message': f'Interval trigger options is invalid'
            }), 400 
            
        if data['trigger'] == "cron" and not vallidate_cron_job_option(data['trigger_options']):
            return jsonify({
                'success': False,
                'message': f'Cron trigger options is invalid'
            }), 400 
            
        return ctl_job_add(data)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
    
    # return ctl_pump_interval_schedule(time_unit, int(amount))

@schedule_blueprint.route("/api/job/remove", methods=["DELETE"])
def route_shed_remove_job():
    data = request.get_json()
    
    if not data or "job_id" not in data:
        return jsonify({
            'success': False,
            "message": f"Empty request body or missing job_id parameter in request body"
        }), 400
        
    job_id = data['job_id']
    return ctl_job_remove(job_id)

@schedule_blueprint.route('/api/pump/schedule/add/interval/<time_unit>/<interval>')
def route_sched_pump_add_job(time_unit: str, amount: int):
    try: 
        data = request.get_json()
        
        if not data:
            return jsonify({
				'success': False,
				'message': 'Empty body'
			}), 400
            
        
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
    
    return ctl_pump_interval_schedule(time_unit, int(amount))

@schedule_blueprint.route('/api/pump/schedule/remove/<job_id>')
def route_sched_pump_remove_job(job_id):
    return ctl_pump_remove_job(job_id)
    