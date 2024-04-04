import asyncio
import socketio
from videoDisplay import playMediaFunction

sio = socketio.AsyncClient(ssl_verify=False)

DEFAULT_URL = 'https://bearmaxcare.com/socket.io/'
# Generate token via cloudflare or self signed and then paste here
# This token essentially plays the same role as the token 'Bearer ...' used for the webscockets where the Bearmax server code is 
token = 'Bot cj0pWScZJqyhQkhnhWwOW772OuxJSFRwHFdfj1O'


async def main():
    await sio.connect(DEFAULT_URL, headers={'Authorization': token}, transports=['polling', 'websocket'])
    print(sio.sid)

    @sio.event
    async def connect():
        print('Connection established')


    @sio.event
    async def connect_error(e):
        print("The connection failed!")
        print(e)


    @sio.event
    async def disconnect():
        print('Disconnected from WebSocket Server')


    @sio.event
    async def speak(msg):
        print(f"ACK: [{msg}]")


    @sio.event
    async def playMedia(mediaURL):
        print(f"Got string for media URL: {mediaURL}")
        playMediaFunction(mediaURL)


    await sio.wait()

asyncio.run(main())