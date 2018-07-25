from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^dashboard/(?P<idnumber>\d+)/$', views.dashboard),
    url(r'^addnewfave/$', views.addnewfave),
    url(r'^createfave/$', views.createfave),
    url(r'^register/$', views.register),
    url(r'^loginProcess/$', views.loginProcess),
    url(r'^follow/(?P<idnumber>\d+)/$', views.follow),
]