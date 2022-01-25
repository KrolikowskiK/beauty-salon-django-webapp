from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class Service(models.Model):
    name = models.CharField("nazwa", max_length=40)
    price = models.DecimalField("cena", max_digits=8, decimal_places=2)

    @admin.display(description="Nazwa usługi")
    def service_name(self):
        return self.name

    @admin.display(description="Cena")
    def service_price(self):
        return self.price

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "usługa"
        verbose_name_plural = "usługi"


class Employee(User):
    employment_date = models.DateField(auto_now_add=True)
    service = models.ForeignKey(
        Service, verbose_name="typ usługi", on_delete=models.SET_NULL, null=True
    )

    @admin.display(description="Imię")
    def employee_first_name(self):
        return self.first_name

    @admin.display(description="Nazwisko")
    def employee_last_name(self):
        return self.last_name

    @admin.display(description="Data zatrudnienia", ordering="employment_date")
    def employee_employment_date(self):
        return self.employment_date

    @admin.display(description="Wykonywana usługa")
    def employee_service(self):
        return self.service

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "pracownik"
        verbose_name_plural = "pracownicy"


class WorkSchedule(models.Model):
    employee = models.ForeignKey(
        Employee, verbose_name="pracownik", on_delete=models.CASCADE
    )
    date = models.DateField("data")

    @admin.display(description="Okres", ordering="date")
    def work_schedule_period(self):
        return self.date.strftime("%m/%Y")

    @admin.display(description="Pracownik")
    def employee_name(self):
        return self.employee

    def __str__(self) -> str:
        employee = self.employee
        date = self.date.strftime("%m/%Y")
        return f"{employee}, {date}"

    class Meta:
        verbose_name = "grafik"
        verbose_name_plural = "grafiki"


class Shift(models.Model):
    work_schedule = models.ForeignKey(WorkSchedule, on_delete=models.CASCADE)
    date = models.DateField("dzień zmiany")
    start = models.TimeField("czas rozpoczęcia")
    end = models.TimeField("czas zakończenia")

    def __str__(self) -> str:
        date = self.date.strftime("%m/%Y")
        start = self.start.strftime("%H:%M")
        end = self.end.strftime("%H:%M")
        return f"Date: {date}, start: {start}, end: {end}"

    class Meta:
        verbose_name = "zmiana"
        verbose_name_plural = "zmiany"


class Appointment(models.Model):
    employee = models.ForeignKey(
        Employee,
        verbose_name="pracownik",
        on_delete=models.CASCADE,
        related_name="employee_appointments",
    )
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="klient",
        on_delete=models.CASCADE,
        related_name="client_appointments",
    )
    date = models.DateTimeField("data wizyty")

    def get_delete_url(self):
        return reverse("appointment-delete", kwargs={"pk": self.id})

    def __str__(self) -> str:
        return f"Wizyta {self.client} u {self.employee} ({self.date.strftime('%d/%m/%Y %H:%M')})"

    class Meta:
        verbose_name = "wizyta"
        verbose_name_plural = "wizyty"


class Opinion(models.Model):
    employee = models.ForeignKey(
        Employee,
        verbose_name="pracownik",
        on_delete=models.CASCADE,
        related_name="employee_opinions",
    )
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="klient",
        on_delete=models.CASCADE,
        related_name="client_opinions",
    )
    text = models.TextField("treść")
    date = models.DateField(auto_now_add=True)

    def get_delete_url(self):
        return reverse("opinion-delete", kwargs={"pk": self.id})

    @admin.display(description="Pracownik")
    def opinion_employee(self):
        return self.employee

    @admin.display(description="Klient")
    def opinion_client(self):
        return self.client

    @admin.display(description="Treść")
    def opinion_text(self):
        return self.text

    @admin.display(description="Data")
    def opinion_date(self):
        return self.date

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = "opinia"
        verbose_name_plural = "opinie"
