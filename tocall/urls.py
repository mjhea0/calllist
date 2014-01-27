from django.conf.urls import patterns, url

from django.views.generic import TemplateView

from tocall import views
from .views import ContactListView, ContactCreateView, HistoryCreateView, HistoryDetailView, HistoryUpdateView, HistoryListView

urlpatterns = patterns('',
	url(
		regex=r'^contact/list/$', 
		view=views.ContactListView.as_view(), 
		name='contact_list'
		),
	url(
		regex=r'^contact/create/$', 
		view=views.ContactCreateView.as_view(), 
		name='contact_add'
		),
	url(
		regex=r'^contact/update/(?P<pk>\d+)/', 
		view=views.ContactUpdateView.as_view(), 
		name='contact_update'
		),
	url(
		regex=r'^contact/(?P<pk>\d+)/', 
		view=views.ContactDetailView.as_view(), 
		name='contact_detail'
		),
    url(
    	regex=r'^history/list/(?P<pk>\d+)/',
    	view=views.HistoryListView.as_view(),
    	name='history_list'
    	),
	url(
		regex=r'^history/(?P<pk>\d+)/', 
		view=views.HistoryDetailView.as_view(), 
		name='history_detail'
		),
	url(
		regex=r'^history/update/(?P<pk>\d+)/', 
		view=views.HistoryUpdateView.as_view(), 
		name='history_update'
		),
    url(
		regex=r'^history/create/(?P<pk>\d+)/', 
		view=views.HistoryCreateView.as_view(), 
		name='history_create'
		),
	url(
		regex=r'^address_book/$', 
		view=views.ContactAddressBookView.as_view(), 
		name='address_book'
		),
	url(
		regex=r'^report/$', 
		view=views.report, 
		name='report'
		),
)