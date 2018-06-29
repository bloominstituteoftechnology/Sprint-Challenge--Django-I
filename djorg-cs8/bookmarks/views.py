from django.shortcuts import render
from .models import Bookmark, PersonalBookmark

# Create your views here.


def index(request):
    pbid = PersonalBookmark.objects.values_list('id')
    context = {}
    context['public_bookmarks'] = Bookmark.objects.exclude(id__in=pbid)
    if request.user.is_anonymous:
        context['private_bookmarks'] = PersonalBookmark.objects.none()
    else:
        context['private_bookmarks'] = PersonalBookmark.objects.filter(
            user=request.user)
    return render(request, 'bookmarks/index.html', context)
