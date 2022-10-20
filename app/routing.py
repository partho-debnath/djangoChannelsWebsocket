from django.urls import path

from . import consumers

websocket_urlpatterns = [ 
    path('ws/app/sc/', consumers.MyWebsocketConsumer.as_asgi()),
    path('ws/app/ac/', consumers.MyAsyncWebsocketConsumer.as_asgi())
]