from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from tocall.models import Contact, History

def index(request):
	return HttpResponse("this is the front page demo.")

def list(request):
	current_list = Contact.objects.order_by('next_call')
	context = {'current_list': current_list}
	return render(request, 'tocall/list.html', context)

def detail(request, id):
	contact = get_object_or_404(Contact, id=id)
	context = {'contact': contact}
	return render(request, 'tocall/detail.html', context)

def address_book(request):
	# addressbook = get_list_or_404(Contact)
	# addressbook.order_by('last_name')
	addressbook = Contact.objects.order_by('last_name')
	context = {'addressbook': addressbook}
	return render(request, 'tocall/addressbook.html', context)

def report(request):
	report = "Here will be some sort of reporting analytics."
	context = {'report': report}
	return render(request, 'tocall/report.html', context)

def effort(request):
	return HttpResponse("Effort page.")
