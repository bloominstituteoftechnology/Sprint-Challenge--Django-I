from django.contrib import admin
from .models import Bookmark, PersonalBookmark

# Register your models here.
admin.site.register(Bookmark)
admin.site.register(PersonalBookmark)
