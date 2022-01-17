from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Appointment
from .forms import AppointmentCreate


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentCreate
    success_url = reverse_lazy("appointment-list")


class AppointmentListView(ListView):
    model = Appointment


class AppointmentDeleteView(DeleteView):
    model = Appointment
    success_url = reverse_lazy("appointment-list")
