from django.shortcuts import render
from .models import Bookmark, Personal_BookMark
from .forms import BookmarkForm


def index(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid(): 
            form.save()

    context = {}

    pbidlist = Personal_BookMark.objects.values_list('id')
    context['bookmarks'] = Bookmark.objects.exclude(id__in=pbidlist)

    if request.user.is_anonymous: 
	    context['personal_bookmarks'] = Personal_BookMark.objects.none()
    else: 
        context['personal_bookmarks'] = Personal_BookMark.objects.filter(user=request.user)

    context['form'] = BookmarkForm

    return render(request, 'bookmarks/index.html', context)