from django.contrib import admin

from omegaTime.models import Worker,Test

# Register your models here.
admin.site.register(Test)
admin.site.register(Worker)