from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='journal.views.index'),
    url(r'(?P<year>[0-9]{4})/$', views.by_year, name='journal.views.by_year'),
    url(r'(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.by_month, name='journal.views.by_month'),
    url(r'(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.by_day, name='journal.views.by_day'),
    url(r'(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<post_id>[0-9]+)$', views.post, name='journal.views.post'),
    url(r'tag/(?P<tag>.+)$', views.by_tag, name='journal.views.by_tag')
]
