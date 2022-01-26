from django import forms
from django.core.exceptions import ValidationError

from .models import Appointment, Employee, Opinion
from .fields import MyModelChoiceField


class EmployeeForm(forms.ModelForm):
    password1 = forms.CharField(
        max_length=150, label="Hasło", widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        max_length=150, label="Potwierdź hasło", widget=forms.PasswordInput()
    )

    class Meta:
        model = Employee
        fields = (
            "email",
            "first_name",
            "last_name",
            "service",
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Hasła nie są takie same!")
        return password2

    def save(self, commit=True, *args, **kwargs):
        employee = super(EmployeeForm, self).save(commit=False, *args, **kwargs)
        employee.set_password(self.cleaned_data["password1"])
        if commit:
            employee.save()
        return employee


class AppointmentCreate(forms.ModelForm):
    employee = MyModelChoiceField(
        queryset=Employee.objects.all(), label="Pracownik i usługa"
    )
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"placeholder": "DD/MM/YYYY HH:MM"}),
        localize=True,
        input_formats=["%d/%m/%Y %H:%M"],
        label="Data i godzina",
    )

    class Meta:
        model = Appointment
        fields = ["employee", "client", "date"]


class OpinionCreateForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ["name", "employee", "text"]
