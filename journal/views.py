from datetime import date

from django.http import Http404
from django.shortcuts import render
from django.utils import formats
from journal.models import Post
from tagging.models import Tag, TaggedItem


def index(request):
    posts = Post.objects.all().order_by('-created')
    tags = [_build_tagged_posts(tag) for tag in Tag.objects.usage_for_model(Post)]
    output = {
        'tags': tags,
        'posts': posts
    }
    return render(request, 'journal.html', output)


def _build_tagged_posts(tag):
    return {
        'name': tag.name,
        'posts': TaggedItem.objects.get_by_model(Post, tag).order_by('-created')
    }


def by_year(request, year):
    posts = Post.objects.filter(created__year=year).order_by('-created')
    output = {
        'filter': year,
        'posts': posts
    }
    return render(request, 'archive.html', output)


def by_month(request, year, month):
    posts = Post.objects.filter(created__year=year, created__month=month).order_by('-created')
    timestamp = date(year=int(year), month=int(month), day=1)
    output = {
        'filter': formats.date_format(timestamp, "F Y"),
        'posts': posts
    }
    return render(request, 'archive.html', output)


def by_day(request, year, month, day):
    posts = Post.objects.filter(created__year=year, created__month=month, created__day=day).order_by('-created')
    timestamp = date(year=int(year), month=int(month), day=int(day))
    output = {
        'filter': formats.date_format(timestamp, "F jS, Y"),
        'posts': posts
    }
    return render(request, 'archive.html', output)


def by_tag(request, tag):
    posts = TaggedItem.objects.get_by_model(Post, tag)
    output = {
        'filter': tag,
        'posts': posts
    }
    return render(request, 'archive.html', output)


def post(request, year, month, day, post_id):
    try:
        p = Post.objects.get(created__year=year, created__month=month, created__day=day, id=post_id)
    except Post.DoesNotExist:
        raise Http404("No post exists with that ID")
    return render(request, 'post.html', {'post': p})
