import asyncio
import socket
import struct
from app.config.config import UDP_PORT, DISCOVERY_MESSAGE
from app.core.state import peers, state_lock
import time

MULTICAST_GROUP = "224.1.1.1"

async def update_peer(ip):
    async with state_lock:
        peers[ip] = time.time()

class PeerDiscoveryProtocol(asyncio.DatagramProtocol):
    def datagram_received(self, data, addr):
        if data.decode() == DISCOVERY_MESSAGE:
            asyncio.create_task(update_peer(addr[0]))

async def listen_for_peers():
    loop = asyncio.get_running_loop()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", UDP_PORT))

    mreq = struct.pack("4sl", socket.inet_aton(MULTICAST_GROUP), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    transport, protocol = await loop.create_datagram_endpoint(
        lambda: PeerDiscoveryProtocol(),
        sock=sock
    )

    try:
        while True:
            await asyncio.sleep(1)
    finally:
        transport.close()
