from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('management', views.management, name='management'),
    path('services', views.services, name='services'),
    path('careers', views.careers, name='careers'),
    path('coexcel', views.coexcel, name='coexcel'),
    path('contactus', views.contactus, name='contactus'),
]
