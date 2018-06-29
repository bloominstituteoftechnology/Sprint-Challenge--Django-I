from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    #TODO: Add User/author
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=20)
    #TODO: Tagging or categories

class PersonalNote(Note):
    user = models.name = models.ForeignKey(User, on_delete=models.CASCADE)
