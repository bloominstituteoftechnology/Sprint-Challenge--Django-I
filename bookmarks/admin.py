from django.contrib import admin
from .models import Bookmark

# Register your models here.

class BookmarkAdmin(admin.ModelAdmin):
    class Meta:
        model = Bookmark

admin.site.register(Bookmark, BookmarkAdmin)