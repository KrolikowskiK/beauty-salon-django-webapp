from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import RegisterView, UserLoginView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
