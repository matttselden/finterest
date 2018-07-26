from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    url(r'^dashboard/(?P<idnumber>\d+)/more_activity$', views.more_activity),
    url(r'^dashboard/(?P<idnumber>\d+)/more_restaurant$', views.more_restaurant),
    url(r'^dashboard/(?P<idnumber>\d+)/more_place$', views.more_place),
    url(r'^unfollow/(?P<idnumber>\d+)/$', views.unfollow),
    url(r'^editprofile/$',views.editprofile)


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
