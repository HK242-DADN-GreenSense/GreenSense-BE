from ..models.threshold_model import TemperatureThreshold
from ..models.notification_model import Notification

class TemperatureMonitor:
    @staticmethod
    def process_temperature_data(temperature_value):
        """
        Process incoming temperature data and create notifications if needed
        """
        try:
            # Convert to float and validate
            temp_value = float(temperature_value)
            
            # Get the most recent threshold
            threshold = TemperatureThreshold.objects.order_by('-updated_at').first()
            if not threshold:
                # Create default if none exists (30°C)
                threshold = TemperatureThreshold(max_threshold=30.0).save()
            
            # Check if temperature exceeds threshold
            if temp_value > threshold.max_threshold:
                # Create notification
                notification = Notification(
                    sensor_type='temperature',
                    message=f'Temperature alert: {temp_value}°C exceeds threshold of {threshold.max_threshold}°C',
                    value=temp_value,
                    threshold=threshold.max_threshold
                ).save()
                
                print(f"Temperature notification created: {notification.message}")
                return True
                
            return False
        except Exception as e:
            print(f"Error processing temperature data: {str(e)}")
            return False