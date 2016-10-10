from datetime import date

from django.http import Http404
from django.shortcuts import render
from django.utils import formats
from journal.models import Post


def index(request):
    posts = Post.objects.all()
    output = {'posts': posts}
    return render(request, 'journal.html', output)


def by_year(request, year):
    posts = Post.objects.filter(created__year=year)
    output = {'period': year,
              'posts': posts}
    return render(request, 'archive.html', output)


def by_month(request, year, month):
    posts = Post.objects.filter(created__year=year,
                                created__month=month)
    timestamp = date(year=int(year), month=int(month), day=1)
    output = {'period': formats.date_format(timestamp, "F Y"),
              'posts': posts}
    return render(request, 'archive.html', output)


def by_day(request, year, month, day):
    posts = Post.objects.filter(created__year=year,
                                created__month=month,
                                created__day=day)
    timestamp = date(year=int(year), month=int(month), day=int(day))
    output = {'period': formats.date_format(timestamp, "F jS, Y"),
              'posts': posts}
    return render(request, 'archive.html', output)


def post(request, year, month, day, post_id):
    try:
        p = Post.objects.get(created__year=year,
                             created__month=month,
                             created__day=day,
                             id=post_id)
    except Post.DoesNotExist:
        raise Http404("No post exists with that ID")
    return render(request, 'post.html', {'post': p})
