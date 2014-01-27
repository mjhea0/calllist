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

class ContactAddressBookView(ListView):
	model = Contact
	template_name_suffix = '_addressbook'

	def get_queryset(self):
		return Contact.objects.filter(user=self.request.user).order_by('last_name')

class ContactDetailView(DetailView):
	model = Contact
	template_name_suffix = "_detail"

	def get_context_data(self, **kwargs):
		context = super(ContactDetailView, self).get_context_data(**kwargs)
		# add the history
		context['history'] = History.objects.filter(contact=self.kwargs.get("pk", None)).order_by('-contacted_at')
		# get_object_or_404(Contact, pk=self.kwargs.get("pk", None)).full_name
		return context


class ContactCreateView(CreateView):
	model = Contact
	fields = ['first_name', 'last_name', 'email', 'mobile', 'next_call']
	template_name_suffix = "_create_form"

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
	model = History

	def get_queryset(self):
		# self.contact = get_object_or_404(Contact, pk=self.kwargs.get("pk", None))
		return History.objects.filter(contact=self.kwargs.get("pk", None)).order_by('-contacted_at')

	def get_context_data(self, **kwargs):
		context = super(HistoryListView, self).get_context_data(**kwargs)
		# add the contact
		context['contact'] = get_object_or_404(Contact, pk=self.kwargs.get("pk", None)).full_name
		return context

class HistoryCreateView(CreateView):
	model = History
	fields = '__all__'
	action = "created"
	template_name_suffix = '_create_form'

	def get_context_data(self, **kwargs):
		context = super(HistoryCreateView, self).get_context_data(**kwargs)
		# add the contact
		context['contact'] = get_object_or_404(Contact, pk=self.kwargs.get("pk", None)).full_name
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
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

def history_item(request, id):
	history = get_object_or_404(History, id=id)
	context = {'history': history}
	return render(request, 'tocall/history_item.html', context)

def edit(request, id):
	contact = get_object_or_404(Contact, id=id)
	return HttpResponseRedirect('tocall/detail.html')

def report(request):
	report = "Here will be some sort of reporting analytics."
	context = {'report': report}
	return render(request, 'tocall/report.html', context)
