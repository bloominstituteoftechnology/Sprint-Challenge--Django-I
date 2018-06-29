from django.contrib import admin

# Register your models here.
from .models import Note, PersonalNote


class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Note

# class NoteUser(user.Model):



admin.site.register((Note, PersonalNote), NoteAdmin)