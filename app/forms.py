from django import forms
from .models import Appointment


class AppointmentCreate(forms.ModelForm):
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"placeholder": "DD/MM/YYYY HH:MM"}),
        localize=True,
        input_formats=["%d/%m/%Y %H:%M"],
    )

    class Meta:
        model = Appointment
        fields = ["employee", "client", "date"]
