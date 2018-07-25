from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^dashboard/$', views.dashboard),
    url(r'^addnewfave/$', views.addnewfave),
    url(r'^register/$', views.register),
    url(r'^loginProcess/$', views.loginProcess),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)