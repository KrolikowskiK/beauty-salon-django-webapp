from django.urls import path

from .views import AppointmentCreateView, AppointmentListView

urlpatterns = [
    path("", AppointmentListView.as_view()),
    path("add/", AppointmentCreateView.as_view()),
]
