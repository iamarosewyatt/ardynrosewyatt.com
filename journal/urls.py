from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<year>[0-9]{4})/$', views.by_year, name='by_year'),
    url(r'(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.by_month, name='by_month'),
    url(r'(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.by_day, name='by_day'),
    url(r'(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<slug>.+)$', views.post, name='post'),
    url(r'tag/(?P<tag>.+)$', views.by_tag, name='by_tag')
]
