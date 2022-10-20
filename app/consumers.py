from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

import json
from time import sleep
import asyncio

class MyWebsocketConsumer(WebsocketConsumer):

    def connect(self):
        print('---------------Synchronous Connection Opened.---------------')
        self.accept()
        # Want to force-close the connection? Call:
        # self.close()
    

    def receive(self, text_data=None, bytes_data=None):
        print(text_data, bytes_data)

        # Or, to send a binary frame:
        # self.send(bytes_data="Hello world!")  # send binary frame not string

        for i in range(1, 21):
            message = {'message': f'ID: {i}'}
            self.send(text_data=json.dumps(message))
            sleep(1)

    def disconnect(self, code):
        print('---------------Synchronous Connection Closed.---------------', code)
        self.close()


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print('---------------Asynchronous Connection Opened.---------------')
        await self.accept()
        # Want to force-close the connection? Call:
        # await self.close()
    

    async def receive(self, text_data=None, bytes_data=None):
        print(text_data, bytes_data)

        # Or, to send a binary frame:
        # await self.send(bytes_data="Hello world!")   # send binary frame not string

        for i in range(1, 21):
            message = {'message': f'ID: {i}'}
            await self.send(text_data=json.dumps(message))
            await asyncio.sleep(1)
    

    async def disconnect(self, code):
        print('---------------Asynchronous Connection Closed.---------------', code)
        await self.close()
        