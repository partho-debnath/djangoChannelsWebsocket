from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class MyWebsocketConsumer(WebsocketConsumer):

    def connect(self):
        print('---------------Synchronous Connection Opened.---------------')
        group_name = self.scope['url_route']['kwargs']['groupName']
        self.group_name = group_name

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

        # Want to force-close the connection? Call:
        # self.close()


    def receive(self, text_data=None, bytes_data=None):

        # self.send(text_data=message)    # send text data
        # Or, to send a binary frame:
        # self.send(bytes_data="Hello world!")   # send binary frame not string

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'chat.message',
                'text': text_data
            }
        )


    def chat_message(self, event):
        message = event['text']
        self.send(text_data=message)


    def disconnect(self, code):
        
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

        # Want to force-close the connection? Call:
        # self.close(code)
        # Or add a custom WebSocket error code!
        # self.close(code=4123)



class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        print('---------------Asynchronous Connection Opened.---------------')

        group_name = self.scope['url_route']['kwargs']['groupName']
        self.group_name = group_name

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        # Want to force-close the connection? Call:
        # await self.accept()


    async def receive(self, text_data=None, bytes_data=None):
        
        print(text_data, bytes_data)

        # await self.send(text_data=message)    # send text data
        # Or, to send a binary frame:
        # await self.send(bytes_data="Hello world!")   # send binary frame not string

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat.message',
                'text': text_data
            }
        )


    async def chat_message(self, event):
        message = event['text']
        await self.send(text_data=message)


    async def disconnect(self, code):
        print('---------------Asynchronous Connection Closed.---------------')

        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

        # Want to force-close the connection? Call:
        await self.close(code)
        # Or add a custom WebSocket error code!
        # await self.close(code=4123)