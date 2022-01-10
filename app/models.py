from django.db import models
from django.conf import settings


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
    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        employee = self.employee
        date = self.date.strftime("%m/%Y")
        return f"{employee}, {date}"


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

    def __str__(self) -> str:
        return f"Wizyta {self.client} u {self.employee} ({self.date.strftime('%d/%m/%Y %H:%M')})"
