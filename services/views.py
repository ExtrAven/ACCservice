from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    services = Service.objects.all()
    return render(request, "index.html", {"services": services})


def services(request):
    return render(request, "services.html")
