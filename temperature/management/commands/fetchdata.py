from django.core.management.base import BaseCommand
from asgiref.sync import sync_to_async
from temperature.models import TemperatureReading

class Command(BaseCommand):
    help = 'Connects to a WebSocket server and processes data synchronously.'
    
    def print_temperature_readings(self):
        # Fetch all temperature readings from the database and orders by timestamp descending
        readings = TemperatureReading.objects.all().order_by('-timestamp')  

        for reading in readings:
            print(f"Temperature: {reading.value}°C, Timestamp: {reading.timestamp}")

    def handle(self, *args, **options):
        self.print_temperature_readings()