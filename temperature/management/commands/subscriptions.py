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

        # Format the time with the UTC offset +00:00
        timestamp = now_utc.isoformat()
        print("time=",timestamp)

        # Create a new TemperatureReading object and save it to the database
        temperature_reading = TemperatureReading(temperature=temperature_value, timestamp=timestamp)
        temperature_reading.save()

        print("Data saved to PostgreSQL:", data)

    # async def capture_data(self):
    #     uri = "ws://localhost:1000/graphql"
    #     start = {
    #         "type": "start",
    #         "payload": {"query": "subscription { temperature }"}
    #     }
    #     async with websockets.connect(uri, subprotocols=["graphql-ws"]) as websocket:
    #         await websocket.send(json.dumps(start))
    #         while True:
    #             data = await websocket.recv()
    #             print("Received data from WebSocket:", data)
    #             # Here you can add your processing logic
    #             self.process_data(json.loads(data))

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
                # Here you can add your processing logic
                self.process_data(json.loads(data))
        finally:
            ws.close()

    def handle(self, *args, **options):
        # asyncio.run(self.capture_data())
        self.capture_data()
