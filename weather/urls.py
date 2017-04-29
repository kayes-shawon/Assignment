from django.conf.urls import url
from . import views
from .views import TempView
urlpatterns = [
    url(r'^temper_form/$', TempView.as_view(), name="inputform"),
    url(r'^tempershow/$', views.get_temperature_show, name='aaa'),
]