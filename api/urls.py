from django.contrib import admin
from django.urls import path, include
from .views import ListSongsView


urlpatterns = [
    # path('', include('api.urls')),
    path('songs/', ListSongsView.as_view(), name="songs-all")
]
