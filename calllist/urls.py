from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tocall import views

urlpatterns = patterns('',
	# url(r'^$', views.index, name='index'),
	# url(r'^(?P<contact_id>\d+)detail/$', views.detail, name='detail'),
	# url(r'^address_book/$', views.address_book, name='address_book'),
	# url(r'^report/$', views.report, name='report'),

    url(r'^tocall/', include('tocall.urls', namespace="tocall")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/auth/$', views.user_login),
    url(r'^accounts/logout/$', views.user_logout, name='logout'),
    url(r'^accounts/register/$', views.user_register),
    url(r'^$', views.index, name='index'),

    # url(r'^accounts/', include('registration.backends.simple.urls', namespace="accounts")),

    # url(r'^$', 'calllist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
)
