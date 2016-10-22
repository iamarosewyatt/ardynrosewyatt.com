from django.conf.urls import url

from cool_stuff import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
