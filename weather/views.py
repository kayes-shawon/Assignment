from weather.forms import TemperForm
from django.views.generic.edit import FormView,CreateView
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


# class TempView(FormView):
#     template_name = 'temper_form.html'
#     form_class = TemperForm
#
#
#     def form_valid(self, form):
#         return super(TempView, self).form_valid(form)
# class TempView(FormView):
#     template_name = 'weather/temper_form.html'
#     form_class = TemperForm
#     success_url = '/weather/index'

class TempView(CreateView):
    template_name = 'weather/temper_form.html'
    form_class = TemperForm
    success_url = '/weather/index'


def get_temperature_ajax(request):
    #load the model
    points = [103, 93, 94, 112, 88, 90]
    labels = ['A', 'B', 'C', 'D', 'E', 'F']
    data = {
        'points': points,
        'labels': labels,
    }
    return JsonResponse(data)



def index(request):
    return render(request=request, template_name='weather/index.html')