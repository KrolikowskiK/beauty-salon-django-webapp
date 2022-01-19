from django.urls import path

from .views import RegisterView, UserLoginView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
]
