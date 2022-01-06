from django.urls import path

from .views import RegisterView, UserLoginView, profile_view

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", UserLoginView.as_view()),
    path("profile/", profile_view),
]
