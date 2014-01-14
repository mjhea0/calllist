from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.forms import ModelForms

from braces.views import LoginRequiredMixin

from .models import Contact, History

class HistoryActionMixin(object):

	@property
	def action(self):
		msg = "{0} is missing action.".format(self.__class__)
		raise NotImplementedError(msg)

	def form_valid(self, form):
		msg = "History {0}!".format(self.action)
		messages.info(self.request, msg)
		return super(HistoryActionMixin, self).form_valid(form)

class HistoryCreateView(LoginRequiredMixin, HistoryActionMixin, CreateView):
	model = History
	action = "created"

class HistoryUpdateView(LoginRequiredMixin, HistoryActionMixin, UpdateView):
	model = History
	action = "updated"

class HistoryDetailView(DetailView):
	model = History

class ContactListView(ListView):
	model = Contact

	def get_context_data(self, **kwargs):
		context = super(ContactListView, self).get_context_data(**kwargs)
		return context

class contact_detail_view(DetailView):
	model = Contact

def list(request):
	current_list = Contact.objects.filter(user=request.user).order_by('next_call')
	context = {'current_list': current_list}
	return render(request, 'tocall/list.html', context)

def detail(request, id):
	contact = get_object_or_404(Contact, id=id)
	history = History.objects.filter(contact=id).order_by('-contacted_at')
	context = {'contact': contact, 'history': history}
	return render(request, 'tocall/detail.html', context)

def history_item(request, id):
	history = get_object_or_404(History, id=id)
	context = {'history': history}
	return render(request, 'tocall/history_item.html', context)

def edit(request, id):
	contact = get_object_or_404(Contact, id=id)
	return HttpResponseRedirect('tocall/detail.html')

def address_book(request):
	addressbook = Contact.objects.filter(user=request.user).order_by('last_name')
	context = {'addressbook': addressbook}
	return render(request, 'tocall/addressbook.html', context)

def report(request):
	report = "Here will be some sort of reporting analytics."
	context = {'report': report}
	return render(request, 'tocall/report.html', context)

