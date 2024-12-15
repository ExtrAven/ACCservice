from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    image = models.ImageField(upload_to="services")

    def __str__(self):
        return self.name
