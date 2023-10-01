from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
from .models import Member

# generated random string should be 10 characters long comprising number and letters
def randomString(stringLength=10):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg= request.POST.get('message')
        # sending email to the user. the company name is halleluya properties limited
        subject = 'Message Received'
        # email message should be string
        message = f"Dear {name.capitalize()}, \nYour Message has been received. \nWe will get back to you shortly. \nThanks for your interest in Halleluya Properties Limited. \nBest Regards, \n\nHalleluya Properties Limited"
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False)
        send_mail(f"Message Alert from {name.capitalize()}", msg + f"\nCustomer email:\n{email}", email, ['halleluyapropertieslimited@gmail.com'], fail_silently=False)
#        send_mail("Message Alert", f"Name: {name}\nEmail: {email}\nMessage: {message}", settings.EMAIL_HOST_USER, ['
        messages.success(request, 'Your Message has been submitted successfully!')
#        return redirect('home')
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
            message = f"Dear {form.cleaned_data.get('full_name')}, \nYour Application has been received. \nYour Application ID is {form_id}. \nWe will get back to you shortly. \nThanks for your interest in Halleluya Properties Limited. \nBest Regards, \n\nHalleluya Properties Limited"
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [form.cleaned_data.get('email')],
                fail_silently=False)
            send_mail("Emploiment Application Alert", "A new application has been received.\nCheck the admin pannel to review the application. \nhttps://www.hplimited.com/admin", settings.EMAIL_HOST_USER, [], fail_silently=False)
            return redirect('home')
    context = {'form': form}
    return render(request, 'application.html', context)


@api_view(['POST'])
def register(request):
    name = request.data.get('name')
    email = request.data.get('email')
    # check if the user already exist by name or email
#    if Member.objects.filter(name=name).exists():
#        return Response({"message": "This name already exist", "status": status.HTTP_400_BAD_REQUEST})
    if Member.objects.filter(email=email).exists():
        return Response({"message": "This email already exist", "status": status.HTTP_400_BAD_REQUEST})
    else:
        # save the user to the database
        member = Member.objects.create(name=name, email=email)
        member.save()
        return Response({"message": "You have successfully registered"})
    