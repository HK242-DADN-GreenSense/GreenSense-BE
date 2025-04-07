from pymongo.collection import Collection 

from ..collection.command_collection import Command, command_collection

def model_insert_command_document(mongo_collection: Collection, command: Command):
    try:
        mongo_collection.insert_one(command)
        
        return True
    except Exception as e:
        print("Error in model_insert_command_document: ", e)
        return False