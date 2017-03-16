from weather.forms import TemperForm
from django.views.generic.edit import FormView

class TempView(FormView):
    template_name = 'temper_form.html'
    form_class = TemperForm


    def form_valid(self, form):
        return super(TempView, self).form_valid(form)
