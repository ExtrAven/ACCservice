from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def index(request):
    services = Service.objects.all()
    return render(request, "index.html", {"services": services})


def service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    service_details = ServiceDetail.objects.filter(service=service)
    return render(
        request, "service.html", {"service": service, "details": service_details}
    )
