from django.shortcuts import render
from whats_coming.model import Item


def index(request):
    items = Item.objects.all().order_by('-created')
    return render(request, 'index.html', {'items': items})
