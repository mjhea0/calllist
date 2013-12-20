from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tocall import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<contact_id>\d+)detail/$', views.detail, name='detail'),
	url(r'^address_book/$', views.address_book, name='address_book'),
	url(r'^report/$', views.report, name='report'),

    url(r'^tocall/', include('tocall.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', 'calllist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
)
