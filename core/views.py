from django.shortcuts import render,redirect
from .models import ContactMessage

# Create your views here.


from .models import Projects

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    project_data = Projects.objects.all()
    return render(request, 'projects.html', {'projects': project_data})

def contacts(request):
    return render(request, 'contacts.html')