from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^journal/', include('journal.urls'), name='journal'),
    url(r'^cool-stuff/', include('cool_stuff.urls')),
    url(r'^whats-coming/', include('whats_coming.urls')),
    url(r'^book/', include('book.urls')),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
