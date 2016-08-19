from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^journal/', include('journal.urls')),
    url(r'^good-stuff/', include('good_stuff.urls')),
]
