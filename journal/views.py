from django.http import Http404
from django.shortcuts import render
from journal.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'journal.html', {'posts': posts})


def post(request, post_id):
    try:
        p = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("No post exists with that ID")
    return render(request, 'post.html', {'post': p})
