from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Member, NewsLetter
from django.core.mail import send_mail
from django.conf import settings

# Signal to send email to new members
@receiver(post_save, sender=Member)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to the Halleluya Properties Limited NewsLetter'
        sender = 'info@halleluyapropertieslimited.com'
        recipient = [instance.email]
        message = f'Welcome to the Halleluya Properties Limited NewsLetter {instance.name}. You have successfully subscribed to our newsletter. Thank you for subscribing.'
        send_mail(subject, message, sender, recipient, fail_silently=False)
        

# whenever a new newsletter is created, send the newsletter to all members. the title is the subject of the email and the content is the message
@receiver(post_save, sender=NewsLetter)
def send_newsletter(sender, instance, created, **kwargs):
    if created:
        subject = instance.title
        sender = 'newsletter@halleluyapropertieslimited.com'
        recipient = [member.email for member in Member.objects.all()]
        message = instance.content
        send_mail(subject, message, sender, recipient, fail_silently=False)