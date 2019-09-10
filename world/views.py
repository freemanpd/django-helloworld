from django.shortcuts import render
from django.http import HttpResponse

def worldView(request):
	return HttpResponse('Hello, World!')
