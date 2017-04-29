from weather.forms import TemperForm
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Temper


class TempView(CreateView):
    template_name = 'weather/temper_form.html'
    form_class = TemperForm
    success_url = '/weather/tempershow/'

def get_temperature_show(request):

    data = Temper.objects.all()
    return render(request,'weather/showtemper.html',{'data':data})

# def get_temperature_ajax(request):
#     #load the model
#     all_temperatures = Temper.objects.all()
#
#     dates_label = []
#     sensor1_temp = []
#     sensor2_temp = []
#     sensor3_temp = []
#     sensor4_temp = []
#
#     for model in all_temperatures:
#         dates_label.append(model.date)
#         sensor1_temp.append(model.sensor1_temp)
#         sensor2_temp.append(model.sensor2_temp)
#         sensor3_temp.append(model.sensor3_temp)
#         sensor4_temp.append(model.sensor4_temp)
#
#     # points = [103, 93, 94, 112, 88, 90]
#     # labels = ['A', 'B', 'C', 'D', 'E', 'F']
#     # data = {
#     #     'points': points,
#     #     'labels': labels,
#     # }
#     data = {
#         'dates': dates_label,
#         'sensor1': sensor1_temp,
#         'sensor2': sensor2_temp,
#         'sensor3': sensor3_temp,
#         'sensor4': sensor4_temp
#     }
#     return JsonResponse(data)


