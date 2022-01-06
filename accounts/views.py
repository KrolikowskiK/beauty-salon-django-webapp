from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    success_url = "/accounts/login"


class UserLoginView(LoginView):
    """
    Manages user sign in with CustomUserAuthenticationForm
    which is passed as an argument to as_view function in mysite/urls.py.
    Redirects user to search page.
    """

    template_name = "accounts/login.html"


def profile_view(request):
    return render(request, "accounts/profile.html")
