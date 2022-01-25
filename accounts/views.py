from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    success_url = "/accounts/login"


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
