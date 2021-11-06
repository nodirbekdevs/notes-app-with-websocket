from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

from ..notes.routing import websocket_urlpatterns
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notes_project.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
})