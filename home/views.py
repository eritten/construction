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



def terms(request):
    return render(request, "terms.html")

def privacy(request):
    return render(request, "privacy.html")







def application(request):
    form = ApplicationForm()
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # generating random form id
            form_id = randomString(10)
            form.instance.form_id = form_id
            form.save()
            messages.success(request, 'Your Application has been submitted successfully!')
            # sending email to the user. the company name is halleluya properties limited
            subject = 'Application Received'
            
            # email message should be string
            message = f"Dear {form.cleaned_data.get('first_name')}, \n\nYour Application has been received. \n\nYour Application ID is {form_id}. \n\nWe will get back to you shortly. \n\nThanks for your interest in Halleluya Properties Limited. \n\nBest Regards, \n\nHalleluya Properties Limited"
            # sending email alert to the company
            # sending email to the company
            return redirect('home')
    context = {'form': form}
    return render(request, 'application.html', context)

