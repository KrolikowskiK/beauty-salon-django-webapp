from django.contrib import admin

from .models import Service, Employee, WorkSchedule, Shift


class ShiftInline(admin.TabularInline):
    model = Shift
    extra = 0


class WorkScheduleAdmin(admin.ModelAdmin):
    inlines = [ShiftInline]


admin.site.register(Service)
admin.site.register(Employee)
admin.site.register(WorkSchedule, WorkScheduleAdmin)
