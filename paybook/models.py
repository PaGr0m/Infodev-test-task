from django.db import models
from .managers import BackendProgrammerManager, \
    DesignerManager, \
    FreelanceCoderManager
import datetime


class Employee(models.Model):
    EMPLOYEE_TYPES = (
        ("BE", "Backend programmer"),
        ("FR", "Freelance coder"),
        ("DSGN", "Designer")
    )

    full_name = models.CharField(verbose_name="full name",
                                 max_length=30)
    employee_type = models.TextField(choices=EMPLOYEE_TYPES)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"


class BackendProgrammer(Employee):
    objects = BackendProgrammerManager()

    class Meta:
        proxy = True


class FreelanceCoder(Employee):
    objects = FreelanceCoderManager()

    class Meta:
        proxy = True


class DesignerProgrammer(Employee):
    objects = DesignerManager()

    class Meta:
        proxy = True


class WageRecord(models.Model):
    month = models.DateField(verbose_name="current month",
                             default=datetime.datetime.now().month)
    year = models.DateField(verbose_name="current year",
                            default=datetime.datetime.now().year)
    salary = models.FloatField(verbose_name="salary")
    employee = models.ForeignKey(to=Employee,
                                 on_delete=models.CASCADE,
                                 verbose_name="employee")
