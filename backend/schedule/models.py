from django.db import models
from backend.pessoal.models import Boss, Worker
# Create your models here.


class TimeTable(models.Model):
    boss = models.ForeignKey(Boss)
    
    
    
class TimeTableLine(models.Model):
    tt = models.ForeignKey(TimeTable)
    start_time = models.DateTimeField(null=True, blank=True)
    worker = models.ForeignKey(Worker)
    end_time = models.DateTimeField(null=True, blank=True)