from django.urls import path

from . import consumers

websocket_urlpatterns = [ 
    path('ws/chat/sc/<str:groupName>/', consumers.MyWebsocketConsumer.as_asgi()),
]