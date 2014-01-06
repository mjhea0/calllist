from django.shortcuts import render
from django.http import HttpResponse

from tocall.models import Contact, History

def index(request):
	return HttpResponse("this is the front page demo.")

def list(request):
	current_list = Contact.objects.order_by('next_call')
	context = {'current_list': current_list}
	return render(request, 'tocall/list.html', context)

def detail(request, id):
	one_contact = Contact.objects.filter(id=id)
	context = {'one_contact': one_contact}
	return render(request, 'tocall/detail.html', context)

def address_book(request):
	return HttpResponse("This is the address_book page.")

def report(request):
	return HttpResponse("Here will be some sort of reporting analytics.")
