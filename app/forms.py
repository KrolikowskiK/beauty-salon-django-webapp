from django import forms
from .models import Appointment


class AppointmentCreate(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["employee", "client", "date"]
