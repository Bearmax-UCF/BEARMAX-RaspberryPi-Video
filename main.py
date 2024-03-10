import socketio
import asyncio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

