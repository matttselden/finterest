from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^dashboard/$', views.dashboard),
    url(r'^addnewfave/$', views.addnewfave),
    url(r'^register/$', views.register),
    url(r'^loginProcess/$', views.loginProcess),
]