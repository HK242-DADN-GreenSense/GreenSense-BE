from mongoengine import Document, FloatField, StringField, DateTimeField, BooleanField
import datetime

class Notification(Document):
    sensor_type = StringField(required=True)  # 'temperature', 'humidity', etc.
    message = StringField(required=True)
    value = FloatField(required=True)  # The actual sensor value
    threshold = FloatField(required=True)  # The threshold that was exceeded
    is_read = BooleanField(default=False)  # Track if user has seen this
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    
    meta = {
        'collection': 'notifications',
        'ordering': ['-created_at']
    }