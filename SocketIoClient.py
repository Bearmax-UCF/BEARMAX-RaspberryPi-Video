import socketio
import asyncio
import aiohttp


DEFAULT_URL = 'https://www.bearmaxcare.com'
# Generate token via cloudflare or self signed and then paste here
token = 'Bot '

class SocketIoClient:
    def __init__(self, url: str, token: str, sio: socketio.AsyncClient):
        self.url = url
        self.token = token
        self.socketioclient = sio
        self.socketHandlers()
    
    async def start(args=None):
        connector = aiohttp.TCPConnector()
        sio = socketio.AsyncClient()
        SockeIOClient = SocketIoClient(DEFAULT_URL, token, sio)

    def socketHandlers(self):    
        @self.socketioclient.event
        async def connect():
            await self.socketioclient.connect(DEFAULT_URL, headers={'Authorization': token})
            print('connection established')

        @sio.event
        async def connect_error():
            print("The connection failed!")

    # Once connection is established, we want to listen for the event
