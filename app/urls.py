from django.urls import path

from .views import (
    AppointmentCreateView,
    AppointmentListView,
    AppointmentDeleteView,
    OpinionCreateView,
    OpinionListView,
    OpinionDeleteView,
)

urlpatterns = [
    path("appointments/", AppointmentListView.as_view(), name="appointment-list"),
    path("appointments/add/", AppointmentCreateView.as_view(), name="appointment-add"),
    path(
        "appointments/<int:pk>/delete/",
        AppointmentDeleteView.as_view(),
        name="appointment-delete",
    ),
    path("opinions/", OpinionListView.as_view(), name="opinion-list"),
    path("opinions/add/", OpinionCreateView.as_view(), name="opinion-add"),
    path(
        "opinions/<int:pk>/delete/", OpinionDeleteView.as_view(), name="opinion-delete"
    ),
]
