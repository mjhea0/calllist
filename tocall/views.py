from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import UpdateView, ModelFormMixin

from braces.views import LoginRequiredMixin
# from crispy_forms.helper import FormHelper
import datetime

from .models import Contact, History
from .forms import UserRegisterForm, HistoryCreateForm, ContactNextCallForm

class ContactActionMixin(object):

	@property
	def action(self):
		msg = "{0} is missing action.".format(self.__class__)
		raise NotImplementedError(msg)

	def form_valid(self, form):
		msg = "Contact {0}!".format(self.action)
		messages.info(self.request, msg)
		return super(ContactActionMixin, self).form_valid(form)

class ContactListView(LoginRequiredMixin, ListView):
	model = Contact

	def get_queryset(self):
		# if the list is done I want a nice big 'Congrtulations! You're done' sign
		return Contact.objects.filter(
			user=self.request.user).filter(
			next_call__lte=datetime.date.today()).order_by('next_call')

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
	fields = ['first_name', 'last_name', 'email', 'mobile', 'introduced_by', 'next_call']
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

class ContactUpdateDateView(ContactUpdateView):
	model = Contact
	fields = ['next_call']
	template_name_suffix = '_update_date_form'
	form_class = ContactNextCallForm

	# def get_queryset(self):
	# 	return History.objects.filter(contact=self.kwargs.get("pk", None)).order_by('-contacted_at')

	# def get_context_data(self, **kwargs):
	# 	context = super(ContactUpdateDateView, self).get_context_data(**kwargs)
	# 	context['contact'] = get_object_or_404(Contact, pk=self.kwargs.get("pk", None)).full_name
	# 	return context

	# def get_initial(self):
	# 	contact = get_object_or_404(Contact, pk=self.kwargs.get("pk", None))
	# 	self = CreateForm(initial={'contact': contact })
	# 	return self.initial.copy()

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


class HistoryListViewTEST(ContactUpdateView):
	model = Contact
	fields = ['next_call']

	def get_queryset(self):
		return History.objects.filter(contact=self.kwargs.get("pk", None)).order_by('-contacted_at')

	def get_context_data(self, **kwargs):
		context = super(HistoryListViewTEST, self).get_context_data(**kwargs)
		# add the contact
		context['contact'] = get_object_or_404(Contact, pk=self.kwargs.get("pk", None)).full_name
		return context

	def get_initial(self):
		contact = get_object_or_404(Contact, pk=self.kwargs.get("pk", None))
		self = HistoryCreateForm(initial={'next_call': next_call })
		return self.initial.copy()



class HistoryCreateView(CreateView):
	model = History
	fields = '__all__'
	form_class = HistoryCreateForm
	action = "created"
	template_name_suffix = '_create_form'

	def get_initial(self):
		contact = get_object_or_404(Contact, pk=self.kwargs.get("pk", None))
		self = HistoryCreateForm(initial={'contact': contact })
		return self.initial.copy()

	def get_context_data(self, **kwargs):
		context = super(HistoryCreateView, self).get_context_data(**kwargs)
		context['contact'] = get_object_or_404(Contact, pk=self.kwargs.get("pk", None))
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
	template_name_suffix = '_detail'

def report(request):
	report = "Here will be some sort of reporting analytics."
	context = {'report': report}
	return render(request, 'tocall/report.html', context)


def index(request):
	c = {}
	c.update(csrf(request))
	c.update({'form':UserRegisterForm()})
	return render_to_response('index.html', c)

# User Login view
def user_login(request):
	if request.user.is_anonymous():
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
            #This authenticates the user
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
                    #This logs him in
					login(request, user)
				else:
					return HttpResponse("Not active")
			else:
				messages.error(request, 'Wrong username/password!')
				c = {}
				c.update(csrf(request))
				c.update({'form':UserRegisterForm()})
				return render_to_response('index.html', c)
	# return HttpResponseRedirect("/")
	return redirect('/tocall/contact/list/')

# User Logout View
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# User Register View
def user_register(request):
    if request.user.is_anonymous():
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('/tocall/contact/create/')
        else:
            form = UserRegisterForm()
        context = {}
        context.update(csrf(request))
        context['form'] = form
        #Pass the context to a template
        return render_to_response('index.html', context)
    else:
        return HttpResponseRedirect('/')