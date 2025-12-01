import asyncio
from app.discovery.UDP_broadcaster import broadcast_presence
from app.discovery.UDP_Listener import listen_for_peers
from app.chat.TCP_Server import start_tcp_server


async def start_background_tasks():
    """Starts necessary tasks in the background"""
    asyncio.create_task(broadcast_presence())
    asyncio.create_task(listen_for_peers())
    asyncio.create_task(start_tcp_server())
