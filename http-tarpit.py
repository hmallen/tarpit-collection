import asyncio
import random

async def handler(_reader, writer):
    writer.write(b'HTTP/1.1 200 OK\r\n')
    try:
        while True:
            await asyncio.sleep(5)
            header = random.randint(0, 2**32)
            value = random.randint(0, 2**32)
            writer.write(b'X-%x: %x\r\n' % (header, value))
            await writer.drain()
    except ConnectionResetError:
        pass

async def main():
    server = await asyncio.start_server(handler, '0.0.0.0', 8080)
    async with server:
        await server.serve_forever()

asyncio.run(main())
