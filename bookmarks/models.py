from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.

class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    url = models.URLField('URL', unique=True, default='')
    name = models.CharField(max_length=200, default='')
    notes = models.TextField(blank=True, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class Personal_BookMark(Bookmark):
    user = models.ForeignKey(User, on_delete=models.CASCADE)