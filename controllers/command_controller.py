from ..collection.command_collection import Command, command_collection
from ..models.command_model import *


def controller_command_test():
    test_collection: Command = {'name': 'test_collection', 'type': 1}
    if not model_insert_command_document(command_collection, test_collection):
        return {
            'success': False,
            'message': 'model_insert_command_document failed to execute'
        }, 400
        
    return {
        'success': True
    }, 200
    
    # command_collection.insert_one(test_collection)