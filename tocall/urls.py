from django.conf.urls import patterns, url

from tocall import views
from .views import ContactListView, HistoryCreateView, HistoryDetailView, HistoryUpdateView

urlpatterns = patterns('',
	# ex: /tocall/
	# url(r'^$', ContactListView.as_view(), name='contact_list'),   # Generic unfiltered, unsorted
	url(
		regex=r'^list/$', 
		view=views.list, 
		name='list'
		),
	url(
		regex=r'^detail/(?P<id>\d+)/', 
		view=views.detail, 
		name='detail'
		),
	url(
		regex=r'^address_book/$', 
		view=views.address_book, 
		name='address_book'
		),
	url(
		regex=r'^history_item/(?P<id>\d+)/', 
		view=views.history_item, 
		name='history_item'
		),
	url(
		regex=r'^report/$', 
		view=views.report, 
		name='report'
		),
	url(
		regex=r'^cbv/(?P<pk>\d+)/', 
		view=views.HistoryUpdateView.as_view(), 
		name='history_update'
		),
    url(
		regex=r'^create/(?P<pk>\d+)/', 
		view=views.HistoryCreateView.as_view(), 
		name='history_create'
		),
)