from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^about/', include('about.urls', namespace='about')),
    url(r'^journal/', include('journal.urls', namespace='journal')),
    url(r'^cool-stuff/', include('cool_stuff.urls', namespace='cool_stuff')),
    url(r'^whats-coming/', include('whats_coming.urls', namespace='whats_coming')),
    url(r'^book/', include('book.urls', namespace='book'))
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
