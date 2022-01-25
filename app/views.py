from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

from .models import Appointment, Opinion, WorkSchedule
from .forms import AppointmentCreate, OpinionCreateForm


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentCreate
    success_url = reverse_lazy("appointment-list")


class AppointmentListView(ListView):
    model = Appointment


class AppointmentDeleteView(DeleteView):
    model = Appointment
    success_url = reverse_lazy("appointment-list")


class OpinionCreateView(View):
    template = "app/opinion_form.html"

    def get(self, request):
        form = OpinionCreateForm(initial={"client": request.user})
        return render(request, self.template, {"form": form})

    def post(self, request):
        form = OpinionCreateForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            redirect("opinion-list")
        return render(request, self.template, {"form": form})


class OpinionListView(ListView):
    model = Opinion


class OpinionDeleteView(DeleteView):
    model = Opinion
    success_url = reverse_lazy("opinion-list")


class WorkScheduleListView(ListView):
    def get_queryset(self):
        return WorkSchedule.objects.filter(employee__email=self.request.user.email)


class WorkScheduleDetailView(DetailView):
    pass
