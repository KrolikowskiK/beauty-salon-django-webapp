from django.contrib import admin

from .models import Service, Employee, WorkSchedule, Shift, Appointment


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service_name", "service_price")


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "employee_employment_date",
        "employee_service",
    )


class ShiftInline(admin.TabularInline):
    model = Shift
    extra = 0


class WorkScheduleAdmin(admin.ModelAdmin):
    inlines = [ShiftInline]
    list_display = ("employee_name", "work_schedule_period")


admin.site.register(Service, ServiceAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(WorkSchedule, WorkScheduleAdmin)
admin.site.register(Appointment)
