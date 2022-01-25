from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Appointment, Opinion, WorkSchedule
from .forms import OpinionCreateForm


class AppointmentCreateView(CreateView):
    model = Appointment
    success_url = reverse_lazy("appointment-list")
    fields = ["employee", "date"]

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


class AppointmentListView(ListView):
    def get_queryset(self):
        return Appointment.objects.filter(client=self.request.user)


class AppointmentDeleteView(DeleteView):
    model = Appointment
    success_url = reverse_lazy("appointment-list")


class OpinionCreateView(CreateView):
    model = Opinion
    form_class = OpinionCreateForm
    success_url = reverse_lazy("intro-view")


class WorkScheduleListView(ListView):
    def get_queryset(self):
        return WorkSchedule.objects.filter(employee__email=self.request.user.email)


class WorkScheduleDetailView(DetailView):
    model = WorkSchedule
