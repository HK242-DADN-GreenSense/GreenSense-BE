from Adafruit_IO import Client, RequestError, Feed

from .. import aio

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