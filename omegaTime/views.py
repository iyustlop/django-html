from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
  return HttpResponse("Index Page")

def worker(request):
  return HttpResponse("Hola mundo")

def worker_name(request, name):
  return HttpResponse("Hola %s" % name) 

def about(request):
  return HttpResponse("About")
