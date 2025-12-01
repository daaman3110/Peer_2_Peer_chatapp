import asyncio

peers = {}
messages = []
state_lock = asyncio.Lock()
