import asyncio
from app.core.state import messages, state_lock


async def handle_client(reader, writer):
    """Reads messages from client and decodes them and appends to messages list"""
    data = await reader.read(1000)
    msg = data.decode()

    async with state_lock:
        messages.append(msg)


async def start_tcp_server():
    """Keeps Running the TCP Server"""
    server = await asyncio.start_server(handle_client, "0.0.0.0", 6000)
    await server.serve_forever()
