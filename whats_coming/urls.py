from django.conf.urls import url

from whats_coming import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
