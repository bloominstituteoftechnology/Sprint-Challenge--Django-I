from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.title} - {self.artist}'


class PersonalSong(Song):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
