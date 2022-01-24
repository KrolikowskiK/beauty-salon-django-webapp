from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField("imię", max_length=150)
    last_name = models.CharField("nazwisko", max_length=150)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
