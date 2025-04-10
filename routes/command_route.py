from flask import Blueprint
from ..controllers.command_controller import *
command = Blueprint('command_blueprint', __name__)

# -------------------- API for command -----------------------

@command.route('/api/command/test', methods=['GET'])
def command_route_test():
    return controller_command_test()