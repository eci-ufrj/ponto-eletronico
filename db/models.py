from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=30, unique=True)
    
class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    position = models.CharField(max_length=50)
    owner = models.ForeignKey(User, related_name='places', related_query_name='place')
    workers = models.ManyToManyField(User, related_name='workplaces', related_query_name='workplace')
    
class TimeCardEntry(models.Model):
    worker = models.ForeignKey(User)
    date = models.DateField(auto_now_add=True)
    start_time = models.TimeField(auto_now_add=True)
    end_time = models.TimeField(blank=True)