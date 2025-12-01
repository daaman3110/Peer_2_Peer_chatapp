import asyncio
from app.config.config import UDP_PORT, DISCOVERY_MESSAGE
from app.core.state import peers, state_lock
import time


class PeerDiscoveryProtocol(asyncio.DatagramProtocol):
    """Peer Discovery Class which gets triggered when it sees the Discovery Message"""

    def connection_made(self, transport):
        self.transport = transport
        print(f"[UDP] Listening on {UDP_PORT}")

    def datagram_received(self, data, addr):
        msg = data.decode()
        ip = addr[0]
        if msg == DISCOVERY_MESSAGE:
            asyncio.create_task(update_peer(ip))


async def update_peer(ip):
    """Update the Peer List with IP and Timestamp"""
    async with state_lock:
        peers[ip] = time.time()


async def listen_for_peers():
    """Listens for peers"""
    # 1: Setting up an engine
    loop = asyncio.get_running_loop()
    # 2: Listening
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: PeerDiscoveryProtocol(), local_addr=("0.0.0.0", UDP_PORT)
    )

    # 3: Keep running forever
    try:
        while True:
            await asyncio.sleep(1)
    finally:
        transport.close()
