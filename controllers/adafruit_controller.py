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
    

def ctl_adafruit_pump(on: bool):
    try:
        pump_feed = aio.feeds('pump')
    except Exception:
        pump = Feed(name='pump')
        pump_feed = aio.create_feed(pump)
        
    try:
        if on:
            aio.send_data(pump_feed.key, 1)
        else:
            aio.send_data(pump_feed.key, 0)
        
        return {
            'success': True
        }, 200
    except Exception as e:
        print("Error while pushing value to Adafruit server")
        return {
            'success': False
        }, 400
        
    