from django.contrib import admin
from .models import Song, PersonalSong

# Register your models here.
admin.site.register(Song)
admin.site.register(PersonalSong)
