from about.models import Moment
from django.shortcuts import render


def index(request):
    moments = Moment.objects.all().order_by('order')
    photos = [moment.image for moment in moments if moment.image]
    return render(request, 'about.html', {'moments': moments, 'photos': photos})
