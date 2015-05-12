from django.conf.urls import include, url
from django.contrib import admin
from apps.tocall import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('calllist_project.apps.tocall.urls')),
    url(r'^accounts/auth/$', views.user_login),
    url(r'^accounts/logout/$', views.user_logout, name='logout'),
    # url(r'^accounts/register/$', views.user_register),
    url(r'^$', views.index, name='index'),
]
