from django.db import models

# Create your models here.


class House(models.Model):
    address = models.CharField(max_length=500)
    gps_location = models.CharField(max_length=50)
