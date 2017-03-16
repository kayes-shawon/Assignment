from django.db import models
#from django.forms import ModelForm
# Create your models here.

class Temper(models.Model):
    date = models.DateField(blank=True, null=True)
    sensor1_temp = models.CharField(max_length=100)
    sensor2_temp = models.CharField(max_length=100)
    sensor3_temp = models.CharField(max_length=100)
    sensor4_temp = models.CharField(max_length=100)

    def __str__(self):
        return self.date


