from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .forms import  ApplicationForm
# importing send_mail function
from django.core.mail import send_mail
from django.contrib import messages
# generating random form id 
import random
import string
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength)) 

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def terms(request):
    return render(request, "terms.html")

def privacy(request):
    return render(request, "privacy.html")

def In_voice(request):
    return render(request, "In_voice.html")






def application(request):
    form = ApplicationForm()
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Application has been submitted successfully!')
        
            return redirect('home')
    context = {'form': form}
    return render(request, 'application.html', context)

