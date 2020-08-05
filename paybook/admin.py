from django.contrib import admin
from django.contrib.admin import register
from .models import Employee, WageRecord


# admin.register(Employee)
# admin.register(WageRecord)


@register(Employee)
class DataAdmin(admin.ModelAdmin):
    list_display = []


@register(WageRecord)
class DeviceAdmin(admin.ModelAdmin):
    list_display = []
