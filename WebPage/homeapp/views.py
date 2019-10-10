from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def management(request):
    return render(request,'management.html',{})

def services(request):
    return render(request,'services.html',{})

def contactus(request):
    return render(request,'contactus.html',{})
