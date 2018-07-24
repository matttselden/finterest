from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^dashboard/$', views.dashboard),
    url(r'^addnewfave/$', views.addnewfave),
]