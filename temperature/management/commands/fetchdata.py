from django.core.management.base import BaseCommand
import asyncio
import websockets
import json
from asgiref.sync import sync_to_async
from temperature.models import TemperatureReading
from datetime import datetime, timezone
from websocket import create_connection

class Command(BaseCommand):
    help = 'Connects to a WebSocket server and processes data asynchronously.'
    
    def print_temperature_readings(self):
        # Fetch all temperature readings from the database
        readings = TemperatureReading.objects.all().order_by('-timestamp')  # Order by timestamp descending

        # Print each reading
        for reading in readings:
            print(f"Temperature: {reading.temperature}°C, Timestamp: {reading.timestamp}")


    def handle(self, *args, **options):
        # asyncio.run(self.capture_data())
        self.print_temperature_readings()
