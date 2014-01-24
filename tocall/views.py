from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect #, HttpResponse
from django.contrib import messages
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import UpdateView #, ModelFormMixin

from braces.views import LoginRequiredMixin
# from crispy_forms.helper import FormHelper

from .models import Contact, History

class ContactActionMixin(object):

	@property
	def action(self):
		msg = "{0} is missing action.".format(self.__class__)
		raise NotImplementedError(msg)

	def form_valid(self, form):
		msg = "Contact {0}!".format(self.action)
		messages.info(self.request, msg)
		return super(ContactActionMixin, self).form_valid(form)

class ContactListView(ListView):
	model = Contact

	def get_queryset(self):
		return Contact.objects.filter(user=self.request.user).order_by('next_call')

class ContactDetailView(DetailView):
	model = Contact
	template_name = "tocall/contact_detail.html"

	def get_context_data(self, **kwargs):
		context = super(ContactDetailView, self).get_context_data(**kwargs)
		# add the history
		context['history'] = History.objects.filter(contact=self.kwargs.get("pk", None)).order_by('-contacted_at')
		# get_object_or_404(Contact, pk=self.kwargs.get("pk", None)).full_name
		return context


class ContactCreateView(CreateView):
	model = Contact
	fields = ['first_name', 'last_name', 'email', 'mobile', 'next_call']
	template_name = "tocall/contact_create.html"

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ContactCreateView, self).form_valid(form)

class ContactUpdateView(ContactActionMixin, UpdateView):
	model = Contact	
	fields = '__all__'
	action = "updated"
	template_name_suffix = '_update_form'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ContactUpdateView, self).form_valid(form)

class HistoryActionMixin(object):

	@property
	def action(self):
		msg = "{0} is missing action.".format(self.__class__)
		raise NotImplementedError(msg)

	def form_valid(self, form):
		msg = "History {0}!".format(self.action)
		messages.info(self.request, msg)
		return super(HistoryActionMixin, self).form_valid(form)

class HistoryListView(ListView):
	# model = History

	def get_queryset(self):
		# self.contact = get_object_or_404(Contact, pk=self.kwargs.get("pk", None))
		return History.objects.filter(contact=self.kwargs.get("pk", None)).order_by('-contacted_at')

	def get_context_data(self, **kwargs):
		context = super(HistoryListView, self).get_context_data(**kwargs)
		# add the contact
		context['contact'] = get_object_or_404(Contact, pk=self.kwargs.get("pk", None)).full_name
		return context

class HistoryCreateView(LoginRequiredMixin, HistoryActionMixin, CreateView):
	model = History

	fields = ['contact', 'write_up', 'email_in', 'email_out', 
		'email_linkedin', 'call_in', 'call_out', 'voice_mail', 'message', 
		'no_message', 'no_answer', 'meeting']
	action = "created"
	# template = 'history_create'

	def form_valid(self, form):
		
		return super(HistoryCreateView, self).form_valid(form)

class HistoryUpdateView(LoginRequiredMixin, HistoryActionMixin, UpdateView):
	model = History
	action = "updated"
	# template = "history_form.html"
	# self.contact = get_object_or_404(Contact, pk=self.kwargs.get("pk", None))

	def form_valid(self, form):
		
		return super(HistoryUpdateView, self).form_valid(form)

class HistoryDetailView(DetailView):
	model = History

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

