from django.contrib import admin

from .models import Bookmark, Personal_BookMark

# Register your models here.
admin.site.register((Bookmark,Personal_BookMark))