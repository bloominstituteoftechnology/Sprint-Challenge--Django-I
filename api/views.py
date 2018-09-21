from django.shortcuts import render
from rest_framework import generics
from .models import Song
from .serializers import SongsSerializer
# Create your views here.


class ListSongsView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongsSerializer
