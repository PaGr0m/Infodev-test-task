from django.db import models
from .managers import \
    BackendProgrammerManager, \
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

    def get_year_salary(self):
        records = Employee.objects.get(id=self.id).wage_records
        print("get::", records)

        return 42

    def get_year_salary_with_tax(self):
        return self.get_year_salary()

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"


class BackendProgrammer(Employee):
    TAX = 0.13
    objects = BackendProgrammerManager()

    def get_year_salary_with_tax(self):
        return self.get_year_salary() * (1 - self.TAX)

    class Meta:
        proxy = True


class FreelanceCoder(Employee):
    TAX = 0.06
    UNIFIED_SOCIAL_TAX = 40_000

    objects = FreelanceCoderManager()

    def get_year_salary_with_tax(self):
        salary_with_tax = self.get_year_salary() * (1 - self.TAX)

        # if salary_with_tax < self.UNIFIED_SOCIAL_TAX:
        #     return self.get_year_salary() - self.UNIFIED_SOCIAL_TAX
        #
        # return salary_with_tax

        return salary_with_tax \
            if salary_with_tax < self.UNIFIED_SOCIAL_TAX \
            else self.get_year_salary() - self.UNIFIED_SOCIAL_TAX

    class Meta:
        proxy = True


class DesignerProgrammer(Employee):
    TAX = 0.06
    objects = DesignerManager()

    def get_year_salary_with_tax(self):
        return self.get_year_salary() * (1 - self.TAX)

    class Meta:
        proxy = True


class WageRecord(models.Model):
    month = models.IntegerField(verbose_name="current month",
                                default=datetime.datetime.now().month)
    year = models.IntegerField(verbose_name="current year",
                               default=datetime.datetime.now().year)
    salary = models.FloatField(verbose_name="salary")
    employee = models.ForeignKey(to=Employee,
                                 related_name="wage_records",
                                 on_delete=models.CASCADE,
                                 verbose_name="employee")
