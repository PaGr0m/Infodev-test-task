import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import QuerySet
from django.db.models import Sum

from .constants import EmployeeConstants
from .managers import \
    BackendProgrammerManager, \
    DesignerManager, \
    FreelanceCoderManager
from currency_converter import CurrencyConverter


class Employee(models.Model, EmployeeConstants):
    full_name = models.CharField(verbose_name="full name",
                                 max_length=30)
    employee_type = models.TextField(choices=EmployeeConstants.EMPLOYEE_TYPES)

    def get_year_salary(self, year):
        records: QuerySet = self.wage_records.filter(year=year)

        if not records.exists():
            raise ObjectDoesNotExist(
                f"There are no salary records for the current year ({year})"
            )

        return float(records.aggregate(
            year_salary=Sum("salary")
        ).get("year_salary", 0))

    def get_year_salary_with_tax(self, year):
        return self.get_year_salary(year)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Staff"


class BackendProgrammer(Employee):
    TAX = 0.13

    objects = BackendProgrammerManager()

    def get_year_salary_with_tax(self, year):
        return self.get_year_salary(year) * (1 - self.TAX)

    class Meta:
        proxy = True


class FreelanceCoder(Employee):
    TAX = 0.06
    UNIFIED_SOCIAL_TAX = 40_000

    objects = FreelanceCoderManager()

    def get_year_salary_with_tax(self, year):
        salary_with_tax = self.get_year_salary(year) * (1 - self.TAX)

        return salary_with_tax \
            if salary_with_tax < self.UNIFIED_SOCIAL_TAX \
            else self.get_year_salary(year) - self.UNIFIED_SOCIAL_TAX

    class Meta:
        proxy = True


class DesignerProgrammer(Employee):
    TAX = 0.06

    objects = DesignerManager()

    def get_year_salary_with_tax(self, year):
        return self.get_year_salary(year) * (1 - self.TAX)

    def currency_conversion(self, year, currency):
        converter = CurrencyConverter()
        return converter.convert(self.get_year_salary(year), "RUB", currency)

    class Meta:
        proxy = True


class WageRecord(models.Model):
    month = models.IntegerField(verbose_name="current month",
                                default=datetime.datetime.now().month)
    year = models.IntegerField(verbose_name="current year",
                               default=datetime.datetime.now().year)
    salary = models.DecimalField(verbose_name="salary",
                                 max_digits=10,
                                 decimal_places=2)
    employee = models.ForeignKey(to=Employee,
                                 related_name="wage_records",
                                 on_delete=models.CASCADE,
                                 verbose_name="employee")

    class Meta:
        verbose_name = "Wage record"
        verbose_name_plural = "Wage records"
        unique_together = ["month", "year", "employee"]
