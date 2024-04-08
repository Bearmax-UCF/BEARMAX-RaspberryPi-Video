import asyncio
import socketio
from videoDisplay import playVideoFunction
from audioVideoDisplay import playAudioVideoFunction
from audioDisplay import playAudioFunction

sio = socketio.AsyncClient()

DEFAULT_URL = 'http://localhost:8080/socket.io/'
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
    async def playMedia(mediaURL, videoBool, audioBool):
        print(f"Got string for media URL: {mediaURL}")
        
        if (videoBool == True and audioBool == True):
            playAudioVideoFunction(mediaURL)
        elif (videoBool == True and audioBool == False):
            playVideoFunction(mediaURL)
        elif (videoBool == False and audioBool == True):
            playAudioFunction(mediaURL)
        else:
            sio.emit("Invalid boolean combo has been provided.")


    await sio.wait()

asyncio.run(main())