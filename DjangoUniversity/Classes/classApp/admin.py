from django.contrib import admin

# Register your models here.
from .models import djangoClasses

admin.site.register(djangoClasses)  # imports the class into the admin site
