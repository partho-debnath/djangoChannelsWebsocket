"""
ASGI config for djangoChannelsWebsocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

from app import routing as approuting
from chat import routing as chatrouting

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoChannelsWebsocket.settings')

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket':URLRouter(
            approuting.websocket_urlpatterns +
            chatrouting.websocket_urlpatterns
        )
    }
)
