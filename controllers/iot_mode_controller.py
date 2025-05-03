from ..common.iot_mode import change_mode, get_modes_info
import subprocess
import os

def ctl_mode_get():
    return get_modes_info(), 200

def ctl_pump_automation(automatic_options):
    change_mode('pump', 'automatic', automatic_options)
    return {
        'success': True,
        'message': "pump mode is currently automatic"
    }, 200

def ctl_pump_manual():
    change_mode('pump', 'manual')
    return {
        'success': True,
        'message': "pump mode is currently manual"
    }, 200
    
# def ctl_fan_automation():
#     change_mode('fan', 'automatic')
#     return {
#         'success': True,
#         'message': "fan mode is currently automatic"
#     }, 200

# def ctl_fan_manual():
#     change_mode('fan', 'manual')
#     return {
#         'success': True,
#         'message': "fan mode is currently manual"
#     }, 200
    
def ctl_servo_automation(automatic_options):
    change_mode('servo', 'automatic', automatic_options)
    return {
        'success': True,
        'message': "servo mode is currently automatic"
    }, 200

def ctl_servo_manual():
    change_mode('servo', 'manual')
    return {
        'success': True,
        'message': "servo mode is currently manual"
    }, 200
    
def ctl_light_automation(automatic_options):
    change_mode('light', 'automatic', automatic_options)
    return {
        'success': True,
        'message': "light mode is currently automatic"
    }, 200

def ctl_light_manual():
    change_mode('light', 'manual')
    return {
        'success': True,
        'message': "light mode is currently manual"
    }, 200
    