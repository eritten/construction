from django.shortcuts import render
from .models import  Project

# Create your views here.
def home(request):
    project = Project.objects.all()
    return render(request, "home.html", {"project": project})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def terms(request):
    return render(request, "terms.html")

def privacy(request):
    return render(request, "privacy.html")
