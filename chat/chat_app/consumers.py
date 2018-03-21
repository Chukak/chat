from channels.generic.websocket import AsyncWebsocketConsumer

import json
import datetime


class ChatConsumer(AsyncWebsocketConsumer):
    """
    Chat consumer.
    1. connect - connects to websocket, open connection.
    2. receive - send message, time, username.
    3. disconnect - close connection.

    """
    async def connect(self):
        await self.accept()
        print(self.scope)
        self.user = self.scope['user']
        print(self.user)

    async def receive(self, text_data=None, bytes_data=None):
        content = json.loads(text_data)
        await self.send(
            json.dumps(
                {
                    'time': datetime.datetime.now().strftime('%H:%M:%S'),
                    'user': self.user.username,
                    'message': content['text'],
                }
            )
        )

    async def disconnect(self, code=None):
        await self.close()
