from django.shortcuts import render

from .models import Note


def index(request):
    notes_list = Note.objects.all()
    print(notes_list)
    context = {'notes_list': notes_list}
    return render(request, 'notes/index.html', context)




