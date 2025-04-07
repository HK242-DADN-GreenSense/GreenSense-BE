import json
from ..config import IOT_ENV
import os

def change_mode(device: str, mode: str) -> None:
    with open(IOT_ENV, 'r') as fopen:
        current_modes = eval(fopen.read())
        
    current_modes[device] = mode
    with open(IOT_ENV, 'w') as fwrite:
        json.dump(current_modes, fwrite)
        
def get_mode(device: str) -> str:
    with open(IOT_ENV, 'r') as fopen:
        current_modes = eval(fopen.read())
    
    if device not in current_modes:
        return ""
    
    return current_modes[device]
        
    