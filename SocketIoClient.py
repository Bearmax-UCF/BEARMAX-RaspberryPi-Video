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

        @self.socketioclient.event
        async def connect_error():
            print("The connection failed!")
        
        @self.socketioclient.event
        async def disconnect():
            self.logger.info('Disconnected from WebSocket Server')

        @self.socketioclient.event
        async def disconnecting():
            self.logger.info('Disconnecting from WebSocket Server')

        @self.socketioclient.event
        async def speak(msg):
            self.publisher_.publish(self.to_msg(f"ACK: [{msg}]"))
        
        @self.sio_.event
        async def ping():
            self.logger.info("Pong!")

        @self.sio_.event
        async def sensoryOverloadAid(action, userID):
            self.logger.info(f"Got aid state command: {action} | {userID}")
            if not action in ("start", "stop"):
                self.logger.error(
                    f"sensoryOverloadAid handler expected string action and got {action}")
            # "aidStart" or "aidStop"
            self.publisher_.publish(self.to_msg(
                "aid" + action.capitalize() + "-" + userID))

        @self.sio_.event
        async def playMedia(mediaURL):
            self.logger.info(f"Got string for media URL: {mediaURL}")
            if not mediaURL.endswith(".mp3") and not mediaURL.endswith(".mp4"):
                self.logger.error("Invalid media file format")
            self.publisher_.publish(self.to_msg(
                "playMedia-" + mediaURL))

    # Once connection is established, we want to listen for the event
