from django.conf.urls import url

from book import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
