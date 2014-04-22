from django.db import models
from backend.places.models import House
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200)
    
    
class Boss(Person):
    house = models.ForeignKey(House)
    
    
class Worker(Person):
    speciality = models.CharField(max_length=100)
    workplaces = models.ManyToManyField(House)
    
