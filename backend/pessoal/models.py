from django.db import models
from backend.places.models import House
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        abstract = True
    
    
class Boss(Person):
    house = models.ForeignKey(House, null=True)
    
    
class Worker(Person):
    speciality = models.CharField(max_length=100, null=True)
    workplaces = models.ManyToManyField(House, null=True)
    
