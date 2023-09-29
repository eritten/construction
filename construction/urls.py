from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
from home.sitemaps import HomeSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.contrib.sitemaps import GenericSitemap

sitemaps = {
    'home': HomeSitemap,
}

urlpatterns = [
path('', views.home, name='home'),
path('privacy/', views.privacy, name='privacy'),
path('terms/', views.terms, name='terms'),
# path('invoice/', views.invoice, name='invoice'),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="sitemap"),
    path("job-application/", views.application, name='job_application'),
    #path('contact/', views.contact, name='contact'),   
]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # urlpatterns += static(settings.MEDIA_ROOT, document_root=MEDIA_ROOT)
