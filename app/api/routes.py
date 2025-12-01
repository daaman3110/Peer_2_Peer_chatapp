from fastapi import APIRouter
from app.core.state import peers, messages
from app.chat.TCP_Client import send_message

router = APIRouter()


@router.get("/peers")
async def get_peers():
    return peers


@router.get("/messages")
async def get_messages():
    return messages


@router.post("/send")
async def send(data: dict):
    ip = data["ip"]
    msg = data["msg"]
    await send_message(ip, msg)
    return {"status": "sent"}
