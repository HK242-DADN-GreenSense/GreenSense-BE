from Adafruit_IO import Client, RequestError, Feed

from .. import aio

def ctl_feed_testing():
    try:
        feed_testing = aio.feeds('testing')
    except Exception:
        feed = Feed(name='testing')
        feed_testing = aio.create_feed(feed)
        
    aio.send_data(feed_testing.key, True)
    
    data = aio.receive_next(feed_testing.key)
    print("receive_next", data)

    data = aio.receive(feed_testing.key)
    print("receive", data)

    data = aio.receive_previous(feed_testing.key)
    print("receive_previous", data)
    
    return {
        'success': True
    }, 200
    

