import asyncio


async def send_message(ip, message):
    """Sends the message to the specified Client based on its individual IP and Port"""
    reader, writer = await asyncio.open_connection(ip, 6000)
    writer.write(message.encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()
