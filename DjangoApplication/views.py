#views.py

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def hello(request):
	return render(request, 'home.html')