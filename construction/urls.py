from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
path('', views.home, name='home'),
path('privacy/', views.privacy, name='privacy'),
path('contact/', views.contact, name='contact'),
path('terms/', views.terms, name='terms'),
path('invoice/', views.invoice, name='invoice'),
    path('admin/', admin.site.urls),
]
