from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("this page lists the contacts by date of next contact.")

def detail(request, id):
	return HttpResponse("This is the detail page for %s." % id)

def address_book(request):
	return HttpResponse("This is the address_book page.")

def report(request):
	return HttpResponse("Here will be some sort of reporting analytics.")
