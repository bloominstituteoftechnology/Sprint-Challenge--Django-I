from rest_framework import serializers, viewsets
from .models import Notes

class NotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notes
        fields = ('title', 'content')

class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()
