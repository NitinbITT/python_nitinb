import websockets
import asyncio

CLIENTS=set()
def handler(websocket):
    CLIENTS.add(websocket)
    try:
        print("Connected websocket")
        websocket.wait_closed()
    finally:
        CLIENTS.remove(websocket)

async def broadcast(message):
    for websocket in CLIENTS.copy():
        try:
            await websocket.send(message)
        except :
            pass        
async def broadcast_message():
    while True:
        message="Hello"
        await broadcast(message)

async def connect():
    async with websockets.serve(handler,"localhost",8000):
        await broadcast_message()

asyncio.run(connect())