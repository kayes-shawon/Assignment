from .models import Temper
from django.forms import ModelForm

class TemperForm(ModelForm):
    class Meta:
        models = Temper
        fields = ['date', 'sensor1_temp', 'sensor2_temp', 'sensor3_temp', 'sensor4_temp']

