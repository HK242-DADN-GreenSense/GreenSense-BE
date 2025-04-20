from mongoengine import Document, FloatField, DateTimeField
import datetime

class TemperatureThreshold(Document):
    max_threshold = FloatField(required=True)  # Trigger notification when temp exceeds this
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)
    
    meta = {
        'collection': 'temperature_thresholds',
        'ordering': ['-updated_at']
    }