from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Note


class NoteConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'notes'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.load(text_data)
        id = text_data_json['id']
        title = text_data_json['title']
        content = text_data_json['content']

        note = Note.objects.get(id=id)
        note.title = title
        note.content = content
        note.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'add_note',
                'id': id,
                'title': title,
                'content': content,
            }
        )

    def add_note(self, event):
        id = event['id']
        title = event['title']
        content = event['content']
        self.send(text_data=json.dumps({
            'id': id,
            'title': title,
            'content': content,
        }))
