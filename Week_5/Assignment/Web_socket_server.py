'''Question 4: WebSocket Chat Server

Create a WebSocket-based chat application with the following features:
Server:

Accept multiple WebSocket client connections
Broadcast messages from one client to all other connected clients
Handle client connection and disconnection gracefully
Assign each client a unique ID
Track and display the number of active connections
Handle malformed messages and connection errors
 
Client:
 
Connect to the WebSocket server
Send messages to the server
Receive and display messages from other clients
Handle disconnection and reconnection'''

import asyncio
from websockets.asyncio.server import serve
import uuid

connected_clients = {}


async def handler(websocket):
    client_id = str(uuid.uuid4())
    connected_clients[client_id] = websocket
    print(f"Client {client_id} is connected")
    print("Active Connections:", len(connected_clients))
    try:
        while True:
            message = await websocket.recv()

            for client,ws in connected_clients.items():
                await ws.send(f"Client({client_id[:4]}):{message}")
    except Exception as e:
        print(e, "Error occured")
    finally:
        print(f"Client {client_id} disconnected")


async def main():
    async with serve(handler, "localhost", 4000) as server:
        print("Server connected at localhost:4000")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
