from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic

from tocall.models import Contact, History

class ContactListView(generic.ListView):
	
	model = Contact

	def get_context_data(self, **kwargs):
		context = super(ContactListView, self).get_context_data(**kwargs)
		return context

class contact_detail_view(generic.DetailView):
	model = Contact

@login_required
def list(request):
	current_list = Contact.objects.filter(user=request.user).order_by('next_call')
	context = {'current_list': current_list}
	return render(request, 'tocall/list.html', context)

@login_required
def detail(request, id):
	contact = get_object_or_404(Contact, id=id)
	context = {'contact': contact}
	return render(request, 'tocall/detail.html', context)

@login_required
def address_book(request):
	addressbook = Contact.objects.filter(user=request.user).order_by('last_name')
	context = {'addressbook': addressbook}
	return render(request, 'tocall/addressbook.html', context)

def report(request):
	report = "Here will be some sort of reporting analytics."
	context = {'report': report}
	return render(request, 'tocall/report.html', context)

def effort(request):
	return HttpResponse("Effort page.")
