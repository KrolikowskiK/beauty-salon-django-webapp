from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Appointment, Opinion, WorkSchedule
from .forms import OpinionCreateForm


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    success_url = reverse_lazy("appointment-list")
    fields = ["employee", "date"]

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


class AppointmentListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Appointment.objects.filter(client=self.request.user)


class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Appointment
    success_url = reverse_lazy("appointment-list")


class OpinionCreateView(LoginRequiredMixin, CreateView):
    model = Opinion
    form_class = OpinionCreateForm
    success_url = reverse_lazy("intro-view")


class WorkScheduleListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return WorkSchedule.objects.filter(employee__email=self.request.user.email)


class WorkScheduleDetailView(LoginRequiredMixin, DetailView):
    model = WorkSchedule
