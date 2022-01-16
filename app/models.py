from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib import admin


class Service(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=40)
    employment_date = models.DateField(auto_now_add=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name


class WorkSchedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self) -> str:
        employee = self.employee
        date = self.date.strftime("%m/%Y")
        return f"{employee}, {date}"

    @admin.display(description="Okres", ordering="date")
    def work_schedule_period(self):
        return self.date.strftime("%m/%Y")

    @admin.display(description="Pracownik")
    def employee_name(self):
        return self.employee


class Shift(models.Model):
    work_schedule = models.ForeignKey(WorkSchedule, on_delete=models.CASCADE)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self) -> str:
        date = self.date.strftime("%m/%Y")
        start = self.start.strftime("%H:%M")
        end = self.end.strftime("%H:%M")
        return f"Date: {date}, start: {start}, end: {end}"


class Appointment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def get_delete_url(self):
        return reverse("author-delete", kwargs={"pk": self.id})

    def __str__(self) -> str:
        return f"Wizyta {self.client} u {self.employee} ({self.date.strftime('%d/%m/%Y %H:%M')})"
