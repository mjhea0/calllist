from django.conf.urls import patterns, url

from tocall import views

urlpatterns = patterns('',
	# ex: /tocall/
	url(r'^$', views.index, name='index'),
	url(r'^list/$', views.list, name='list'),
	url(r'^detail/(?P<id>\d+)/', views.detail, name='detail'),
	url(r'^address_book/$', views.address_book, name='address_book'),
	url(r'^report/$', views.report, name='report'),
)