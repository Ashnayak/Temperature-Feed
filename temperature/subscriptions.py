import asyncio
import json
import websockets
from temperature.models import TemperatureReading 

async def process_data(data):
    """
    Process the subscription data received from the WebSocket server and save it to PostgreSQL.
    
    Parameters:
        data (dict): The data received from the WebSocket server.

    Returns:
        None
    """
    # Extract relevant information from the data
    temperature_value = data.get('temperature')
    timestamp = data.get('timestamp')

    # Create a new TemperatureReading object and save it to the database
    temperature_reading = TemperatureReading(temperature=temperature_value, timestamp=timestamp)
    temperature_reading.save()

    print("Data saved to PostgreSQL:", data)


async def capture_data():
    uri = "ws://localhost:1000/graphql"
    start = {
        "type": "start",
        "payload": {"query": "subscription { temperature }"}
    }
    async with websockets.connect(uri, subprotocols=["graphql-ws"]) as websocket:
        await websocket.send(json.dumps(start))
        while True:
            data = await websocket.recv()
            # Process and store data in the database
