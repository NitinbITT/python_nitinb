import asyncio
import websockets
 
async def run():
    async with websockets.connect("ws://172.22.0.33:8765") as ws:
        while True:
            message=input()
            await ws.send(message)
            reply = await ws.recv()
            print(reply)
       
asyncio.run(run())
 