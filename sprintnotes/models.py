from django.db import models
from uuid import uuid4

class Note(models.Model):
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=300)
    id = models.UUIDField(primary_key=True, default=uuid4)



