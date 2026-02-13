import websockets
import asyncio

async def websocket_connect(websockets):
    try:
        while True:
            message=await websockets.recv()

            print("Client:",message)

    except Exception as e:
            print(e,"An error occured")

async def web():
    async with websockets.serve(websocket_connect,"localhost",8000):
        print("Connected websocket at localhost:8000")
        await asyncio.Future()

asyncio.run(web())