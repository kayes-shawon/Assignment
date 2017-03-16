from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^temper_form/$', TemplateView.as_view(template_name="temper_form.html")),
]