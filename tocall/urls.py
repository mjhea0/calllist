from django.conf.urls import patterns, url

from tocall import views
from tocall.views import ContactListView

urlpatterns = patterns('',
	# ex: /tocall/
	url(r'^$', ContactListView.as_view(), name='contact_list'),
	url(r'^list/$', views.list, name='list'),
	url(r'^detail/(?P<id>\d+)/', views.detail, name='detail'),
	url(r'^address_book/$', views.address_book, name='address_book'),
	url(r'^effort/(?P<id>\d+)/', views.effort, name='effort'),
	url(r'^report/$', views.report, name='report'),
)