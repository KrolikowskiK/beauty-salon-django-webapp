from django.urls import path

from .views import RegisterView, UserLoginView, profile_view

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", profile_view),
]
