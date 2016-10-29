from django.shortcuts import render
from whats_coming.models import Item


def index(request):
    items = Item.objects.all().order_by('-created')
    return render(request, 'whats-coming.html', {'items': items})
