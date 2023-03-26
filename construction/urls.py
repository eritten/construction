from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', views.home, name='home'),
path('privacy/', views.privacy, name='privacy'),
path('contact/', views.contact, name='contact'),
path('terms/', views.terms, name='terms'),
path('invoice/', views.invoice, name='invoice'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
