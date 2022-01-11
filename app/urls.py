from django.urls import path

from .views import AppointmentCreateView, AppointmentListView, AppointmentDeleteView

urlpatterns = [
    path("", AppointmentListView.as_view(), name="appointment-list"),
    path("add/", AppointmentCreateView.as_view(), name="appointment-add"),
    path("<int:pk>/delete/", AppointmentDeleteView.as_view(), name="author-delete"),
]
