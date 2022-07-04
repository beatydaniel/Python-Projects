from django.contrib import admin

# Register your models here.
from .models import Account
from .models import Information

admin.site.register(Account)
admin.site.register(Information)