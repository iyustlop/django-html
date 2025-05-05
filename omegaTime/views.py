from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Worker, Account
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
  return render(request, 'index.html')

def worker(request):
  workers = list(Worker.objects.values())
  return JsonResponse(workers, safe=False)

def worker_name(request, name):
  worker = get_object_or_404(Worker, name=name)
  return HttpResponse("Hola %s" % worker.name)

def about(request):
  return HttpResponse("About")
