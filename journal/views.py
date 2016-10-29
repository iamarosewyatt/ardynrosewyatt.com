from datetime import date

from django.http import Http404
from django.shortcuts import render
from django.utils.formats import date_format
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
    posts = Post.objects.filter(created__year=year).order_by('created')
    return archive(request, year, posts)


def by_month(request, year, month):
    created_at = '{}-{}'.format(year, zero_pad(month))
    posts = Post.objects.filter(created__contains=created_at).order_by('created')
    timestamp = date(year=int(year), month=int(month), day=1)
    return archive(request, date_format(timestamp, "F Y"), posts)


def by_day(request, year, month, day):
    created_at = '{}-{}-{}'.format(year, zero_pad(month), zero_pad(day))
    posts = Post.objects.filter(created__contains=created_at).order_by('created')
    timestamp = date(year=int(year), month=int(month), day=int(day))
    return archive(request, date_format(timestamp, "F jS, Y"), posts)


def by_tag(request, tag):
    posts = TaggedItem.objects.get_by_model(Post, tag).order_by('-created')
    return archive(request, tag, posts)


def archive(request, key, posts):
    return render(request, 'archive.html', {
        'filter': key,
        'posts': posts
    })


def post(request, year, month, day, slug):
    try:
        created_at = '{}-{}-{}'.format(year, zero_pad(month), zero_pad(day))
        p = Post.objects.get(created__contains=created_at, slug=slug)
    except Post.DoesNotExist:
        timestamp = date(year=int(year), month=int(month), day=int(day))
        raise Http404('No post exists with slug "{}" on {}'.format(slug, date_format(timestamp, "F jS, Y")))
    return render(request, 'post.html', {'post': p})


def zero_pad(number):
    if len(number) == 1:
        return '0{}'.format(number)
    else:
        return number
