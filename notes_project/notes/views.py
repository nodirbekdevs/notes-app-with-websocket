from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def get_notes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_note_counts(request):
    notes = Note.objects.all().count()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_note(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def make_note(request):
    data = request.data
    note = Note.objects.create(
        title=data['title'],
        content=data['content']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def update_note(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    note.title=data['title']
    note.content=data['content']
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def update_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response({message: 'Note was deleted'})
    return Response(serializer.data)
