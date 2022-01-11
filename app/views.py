from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Appointment
from .forms import AppointmentCreate


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentCreate
    success_url = "/appointments/"


class AppointmentListView(ListView):
    model = Appointment
