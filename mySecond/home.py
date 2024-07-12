from django.http import HttpResponse
from django.shortcuts import render

def dungen(request):
	return render(request, "home.html") 