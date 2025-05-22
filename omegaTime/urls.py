from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('worker/', views.worker),
    path('worker/<str:name>', views.worker_name, name='worker_name'),
    path('about/', views.about)
]