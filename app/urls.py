from django.urls import path

from .views import (
    AppointmentCreateView,
    AppointmentListView,
    AppointmentDeleteView,
    OpinionCreateView,
    WorkScheduleListView,
    WorkScheduleDetailView,
)

urlpatterns = [
    path(
        "appointments/",
        AppointmentListView.as_view(),
        name="appointment-list",
    ),
    path(
        "appointments/add/",
        AppointmentCreateView.as_view(),
        name="appointment-add",
    ),
    path(
        "appointments/<int:pk>/delete/",
        AppointmentDeleteView.as_view(),
        name="appointment-delete",
    ),
    path(
        "opinions/add/",
        OpinionCreateView.as_view(),
        name="opinion-add",
    ),
    path(
        "work-schedules/",
        WorkScheduleListView.as_view(),
        name="workschedule-list",
    ),
    path(
        "work-schedules/<int:pk>/",
        WorkScheduleDetailView.as_view(),
        name="workschedule-detail",
    ),
]
