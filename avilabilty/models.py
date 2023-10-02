from django.db import models



class Shift(models.Model):
    # Day of week
     day = models.CharField(max_length=100)
    # Morning, afternoon, evening
     time = models.CharField(max_length=100)    

# Create your models here.
class Employee(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    availability = models.ManyToManyField(Shift)
