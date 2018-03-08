from channels.generic.websocket import WebsocketConsumer

import json
import datetime


class ChatConsumer(WebsocketConsumer):
    """
    Chat consumer.
    1. connect - connects to websocket, open connection.
    2. receive - send message, time, username.
    3. disconnect - close connection.

    """
    def connect(self):
        self.accept()
        self.user = self.scope['user']

    def receive(self, text_data=None, bytes_data=None):
        content = json.loads(text_data)
        self.send(
            json.dumps(
                {
                    'time': datetime.datetime.now().strftime('%H:%M:%S'),
                    'user': self.user.username,
                    'message': content['text'],
                }
            )
        )

    def disconnect(self, code=None):
        self.close()
