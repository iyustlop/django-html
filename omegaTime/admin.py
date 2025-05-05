from django.contrib import admin

from omegaTime.models import Account, Worker

# Register your models here.
admin.site.register(Worker)
admin.site.register(Account)