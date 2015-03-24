from django.conf.urls import patterns, url
from weekly import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
