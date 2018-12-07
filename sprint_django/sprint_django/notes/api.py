from rest_framework import serializers, viewsets
from notes.models import PersonalNote
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = PersonalNote
        fields = ('title', 'content')
class api_view(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all() 
    def snippet_list(request):
        if request.method == 'GET':
             snippets = PersonalNote.objects.all()
             serializer = PersonalNoteSerializer(snippets, many=True)
             return Response(queryset)
             

