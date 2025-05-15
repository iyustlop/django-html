from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Test, Worker
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
  return render(request, 'index.html')

def worker(request):
  workers = list(Test.objects.values())
  return render(request, 'workers.html', {
    'workers': workers
  })

def worker_name(request, name):
  worker = get_object_or_404(Test, name=name)
  return render(request, 'worker.html')

def about(request):
  return render(request, 'about.html')
