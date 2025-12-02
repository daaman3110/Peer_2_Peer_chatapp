import asyncio
import socket
from app.config.config import UDP_PORT, DISCOVERY_MESSAGE, BROADCAST_INTERVAL


async def broadcast_presence():
    # 1: Creating a UDP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2: Enabling Broadcasting
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Sending the broadcast message every "BROADCAST INTERVAL" seconds
    while True:
        # 3: Sending a broadcast message
        sock.sendto(DISCOVERY_MESSAGE.encode(), ("<broadcast>", UDP_PORT))
        await asyncio.sleep(BROADCAST_INTERVAL)
