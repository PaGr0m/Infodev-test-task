from django.contrib import admin
from django.contrib.admin import register
from .models import Employee, WageRecord


# admin.site.register(Employee)
# admin.site.register(WageRecord)

@register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "employee_type"
    ]


@register(WageRecord)
class WageRecordAdmin(admin.ModelAdmin):
    list_display = [
        "month",
        "year",
        "salary",
        "employee"
    ]
