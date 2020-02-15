from django.shortcuts import render
from .models import Comments
from .forms import CommentForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def management(request):
    return render(request,'management.html',{})

def services(request):
    return render(request,'services.html',{})

def careers(request):
    return render(request,'careers.html',{})

def coexcel(request):
    return render(request,'coexcel.html',{})

def contactus(request):

    if request.method == 'POST':
        form = CommentForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = Comments.objects.all
            messages.success(request,('Comment has successfully been added!'))
            return render(request,'contactus.html',{'all_items' : all_items})

    else:
        all_items = Comments.objects.all
        return render(request,'contactus.html',{'all_items' : all_items})
