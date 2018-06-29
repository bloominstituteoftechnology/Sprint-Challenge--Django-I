from django.db import models
from uuid import uuid4
# from django.contrib.auth.models import User

# Create your models here.

class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    nickname = models.CharField(max_length = 50)
    url = models.URLField(max_length = 200)
    description = models.CharField(max_length = 100)