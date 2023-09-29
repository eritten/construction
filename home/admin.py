from django.contrib import admin
from .models import Application
# Register your models here.


admin.site.register(Application)


admin.site.site_header = "Halleluya properties limited admin Panel"
admin.site.site_title = "Halleluya properties limited admin Panel"
admin.site.index_title = "Welcome to Halleluya properties limited admin Panel"

