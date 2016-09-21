from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^journal/', include('journal.urls')),
    url(r'^cool-stuff/', include('cool_stuff.urls')),
    url(r'^more-cool-stuff/', include('more_cool_stuff.urls')),
    url(r'^book/', include('book.urls')),
]
