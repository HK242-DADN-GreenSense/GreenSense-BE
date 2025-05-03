import json
from ..config import IOT_ENV
import os

def change_mode(device: str, mode: str, options: dict | None = None) -> None:
    with open(IOT_ENV, 'r') as fopen:
        current_modes = json.load(fopen)
        
    current_modes[device]['mode'] = mode
    
    if options:
        current_modes[device]['automatic_options'] = options
    else:
        current_modes[device]['automatic_options'] = None
        
    
    with open(IOT_ENV, 'w') as fwrite:
        json.dump(current_modes, fwrite)
        
def get_mode(device: str) -> str:
    with open(IOT_ENV, 'r') as fopen:
        current_modes = json.load(fopen)
    
    if device not in current_modes:
        return ""
    
    return current_modes[device]['mode']

def get_automatic_options(device: str) -> dict | None:
    with open(IOT_ENV, 'r') as fopen:
        current_modes = json.load(fopen)
    
    if device not in current_modes:
        return None
    
    return current_modes[device]['automatic_options']
        
def get_modes_info() -> dict:
    with open(IOT_ENV, 'r') as fopen:
        current_modes = json.load(fopen)

    return current_modes