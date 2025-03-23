from Adafruit_IO import Client, RequestError, Feed

from .. import aio

def ctl_feed_testing(spped):
    try:
        feed_testing = aio.feeds('fan')
    except Exception:
        feed = Feed(name='fan')
        feed_testing = aio.create_feed(feed)
        
    aio.send_data(feed_testing.key, 0)
    
    # data = aio.receive_next(feed_testing.key)
    # print("receive_next", data)

    # data = aio.receive(feed_testing.key)
    # print("receive", data)

    # data = aio.receive_previous(feed_testing.key)
    # print("receive_previous", data)
    
    return {
        'success': True
    }, 200

def ctl_servo(angle):
    """Control servo position via Adafruit IO feed"""
    # Validate angle is within servo range
    if not isinstance(angle, (int, float)) or angle < 0 or angle > 180:
        return {
            'success': False,
            'message': 'Angle must be between 0 and 180'
        }, 400
    
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
            'success': True
        }, 200
    except Exception as e:
        print("Error while pushing value to Adafruit server")
        return {
            'success': False
        }, 400
        
def send_fan_req(speed):
    try:
        feed_testing = aio.feeds('fan')
    except Exception:
        feed = Feed(name='fan')
        feed_testing = aio.create_feed(feed)
    try: 
        intspeed = int(speed)
        if (intspeed >= 0 and intspeed <= 255):
            aio.send_data(feed_testing.key, intspeed)
        
            return {
                'success': True
        }, 200
    except Exception:
        return {
            'success': False
        }, 400