from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async


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




    def receive(self, text_data=None, bytes_data=None):
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
        return super().disconnect(code)