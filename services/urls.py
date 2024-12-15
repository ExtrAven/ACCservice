from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("service/<int:service_id>/", service, name="service"),
]
