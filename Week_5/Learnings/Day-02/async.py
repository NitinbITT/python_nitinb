import asyncio 
import time
async def aschronous():
    print("Into the function")
    await asyncio.sleep(3)
    print("completed fucntion")

def normal():
    print("Normal function")
    time.sleep(2)
    print("Completed normal function")
asyncio.run(aschronous())
normal()