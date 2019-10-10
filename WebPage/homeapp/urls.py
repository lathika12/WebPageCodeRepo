from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('management', views.management, name='management'),
    path('services', views.services, name='services'),
    path('contactus', views.contactus, name='contactus'),
]
