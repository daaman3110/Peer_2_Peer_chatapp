import asyncio
import socket
import struct
from app.config.config import UDP_PORT, DISCOVERY_MESSAGE, BROADCAST_INTERVAL

MULTICAST_GROUP = "224.1.1.1"

async def broadcast_presence():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

    print(f"[UDP] Multicasting to {MULTICAST_GROUP}:{UDP_PORT}")

    while True:
        sock.sendto(DISCOVERY_MESSAGE.encode(), (MULTICAST_GROUP, UDP_PORT))
        await asyncio.sleep(BROADCAST_INTERVAL)
