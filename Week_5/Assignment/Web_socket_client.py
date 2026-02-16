import asyncio
from websockets.asyncio.client import connect


async def receive_message(conn):
    while True:
        try:
            server_message = await conn.recv()
            print(server_message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break


async def send_message(conn):
    while True:
        try:
            message = await asyncio.to_thread(input)
            await conn.send(message)
        except Exception as e:
            print(f"Error sending message: {e}")
            break


async def main():
    uri = "ws://localhost:4000"
    async with connect(uri) as conn:
        await asyncio.gather(send_message(conn), receive_message(conn))


if __name__ == "__main__":
    asyncio.run(main())
