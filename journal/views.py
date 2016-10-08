from django.shortcuts import render
from journal.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'journal.html', {'posts': posts})
