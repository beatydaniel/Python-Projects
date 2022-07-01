from django.shortcuts import render
from .models import Profile

# Create your views here.

def home(request):
    return render(request,"home.html")

def admin_console(request):
    profiles = Profile.objects.all()
    return render(request, 'home.html', {'profiles': profiles})