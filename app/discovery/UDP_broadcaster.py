import asyncio
import socket
from app.config.config import UDP_PORT, DISCOVERY_MESSAGE, BROADCAST_INTERVAL


def get_lan_ip():
    """Return the IP of the active LAN interface."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # This does NOT send packets; it's a trick to get the LAN interface
        s.connect(("192.168.0.1", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "0.0.0.0"


async def broadcast_presence():
    lan_ip = get_lan_ip()

    # Determine broadcast (example -> 192.168.0.255)
    broadcast_ip = lan_ip.rsplit(".", 1)[0] + ".255"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Bind only to LAN interface
    sock.bind((lan_ip, 0))

    print(f"[UDP] Broadcasting from {lan_ip} → {broadcast_ip}")

    while True:
        sock.sendto(DISCOVERY_MESSAGE.encode(), (broadcast_ip, UDP_PORT))
        await asyncio.sleep(BROADCAST_INTERVAL)
