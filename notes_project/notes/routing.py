from django.urls import path

from .consumers import NoteConsumer


websocket_urlpatterns = [
    path('ws/notes/', NoteConsumer)
]