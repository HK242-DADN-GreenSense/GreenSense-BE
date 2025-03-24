from Adafruit_IO import Client, RequestError, Feed

from .. import aio

def ctl_adafruit_servo(angle):
    """Control servo position via Adafruit IO feed"""
    # Validate angle is within servo range
    if angle < 0 or angle > 180:
        return {
            'success': False,
            'message': 'Angle must be between 0 and 180'
        }, 400
        
    if not isinstance(angle, int):
        return {
            'success': False,
            'message': 'Angle must be a number'
        }
    
    try:
        # Get or create the servo feed
        try:
            servo_feed = aio.feeds('servo')
        except Exception:
            feed = Feed(name='servo')
            servo_feed = aio.create_feed(feed)
        
        # Send angle value to the feed
        aio.send_data(servo_feed.key, angle)
        
        return {
            'success': True,
            'angle': angle
        }, 200
        
    except Exception as e:
        return {
            'success': False,
            'message': str(e)
        }, 500

def ctl_adafruit_pump(status: str):
    if status not in ['on', 'off']:
        return {
            'success': False,
            'message': 'status value must be "on" or "off"'
        }, 400
    
    try:
        pump_feed = aio.feeds('pump')
    except Exception:
        pump = Feed(name='pump')
        pump_feed = aio.create_feed(pump)
        
    try:
        if status == 'on':
            aio.send_data(pump_feed.key, 1)
        elif status == 'off':
            aio.send_data(pump_feed.key, 0)
            
        return {
            'success': True,
            'pump_status': status
        }, 200
    except Exception as e:
        print("Error while pushing value to Adafruit server")
        return {
            'success': False
        }, 500
        
def ctl_adafruit_fan(speed):
    if speed < 0 or speed > 255:
        return {
            'success': False,
            'message': 'Speed must be between 0 and 255'
        }, 400
        
    if not isinstance(speed, int):
        return {
            'success': False,
            'message': 'Speed must be a number'
        }, 400 

    try:
        feed_testing = aio.feeds('fan')
    except Exception:
        feed = Feed(name='fan')
        feed_testing = aio.create_feed(feed)
        
    try: 
        aio.send_data(feed_testing.key, speed)
            
        
        return {
            'success': True,
            'current_fan_speed': speed
        }, 200
    except Exception as e:
        return {
            'success': False,
            'message': str(e)
        }, 500