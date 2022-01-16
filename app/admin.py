from django.contrib import admin

from .models import Service, Employee, WorkSchedule, Shift, Appointment


class ShiftInline(admin.TabularInline):
    model = Shift
    extra = 0


class WorkScheduleAdmin(admin.ModelAdmin):
    inlines = [ShiftInline]
    list_display = ("employee_name", "work_schedule_period")


admin.site.register(Service)
admin.site.register(Employee)
admin.site.register(WorkSchedule, WorkScheduleAdmin)
admin.site.register(Appointment)
