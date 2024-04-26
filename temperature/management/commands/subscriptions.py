from django.core.management.base import BaseCommand
import json
import websockets
from temperature.models import TemperatureReading
from datetime import datetime, timezone
from websocket import create_connection

class Command(BaseCommand):
    help = 'Connects to a WebSocket server and processes data asynchronously.'

    def process_data(self,data):
        """
        Process the subscription data received from the WebSocket server and save it to PostgreSQL.
        
        Parameters:
            data (dict): The data received from the WebSocket server.

        Returns:
            None
        """
        # Extract relevant information from the data
        print("data",data)
        temperature_value = data['payload']['data']['temperature']
        now_utc = datetime.now(timezone.utc)

        # Format time with UTC offset +00:00
        timestamp = now_utc.isoformat()
        print("time=",timestamp)

        # Create a new TemperatureReading object and save it to the database
        temperature_reading = TemperatureReading(temperature=temperature_value, timestamp=timestamp)
        temperature_reading.save()

        print("Data saved to PostgreSQL:", data)

    def capture_data(self):
        uri = "ws://localhost:1000/graphql"
        start = {
            "type": "start",
            "payload": {"query": "subscription { temperature }"}
        }

        # Create a synchronous WebSocket connection
        ws = create_connection(uri, subprotocols=["graphql-ws"])
        try:
            ws.send(json.dumps(start))
            while True:
                data = ws.recv()
                print("Received data from WebSocket:", data)
                self.process_data(json.loads(data))
        finally:
            ws.close()

    def handle(self, *args, **options):
        self.capture_data()
