from django.db import models

# Create your models here.
class Worker(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=50)
  location = models.CharField(max_length=50)

class Test(models.Model):
  language = models.CharField(max_length=100)
  status = models.CharField(max_length=50, default="Madrid")
  worker = models.ForeignKey(Worker, on_delete=models.CASCADE)