from django.db import models

# Create your models here.
class Worker(models.Model):
  name = models.CharField(max_length=200)

class Account(models.Model):
  account = models.CharField(max_length=100)
  worker = models.ForeignKey(Worker, on_delete=models.CASCADE)