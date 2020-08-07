import unittest

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from .constants import EmployeeConstants
from .models import Employee, BackendProgrammer, DesignerProgrammer, \
    FreelanceCoder, WageRecord


class EmployeeTestCase(TestCase):
    def test_check_employee_type(self):
        employee1 = Employee.objects.create(
            id=666,
            employee_type=EmployeeConstants.BACKEND_PROGRAMMER,
            full_name="Another name"
        )
        employee2 = Employee.objects.create(
            id=777,
            employee_type=EmployeeConstants.DESIGNER,
            full_name="Qwerty qwerty"
        )

        self.assertEqual(Employee.objects.all().count(), 2)
        self.assertEqual(BackendProgrammer.objects.all().count(), 1)
        self.assertEqual(DesignerProgrammer.objects.all().count(), 1)
        self.assertEqual(FreelanceCoder.objects.all().count(), 0)

    def test_year_salary(self):
        emp = BackendProgrammer.objects.create(
            id=666,
            employee_type=EmployeeConstants.BACKEND_PROGRAMMER,
            full_name="Another name"
        )
        wage1 = WageRecord.objects.create(
            employee=emp,
            year=2020,
            month=2,
            salary=12345
        )
        wage2 = WageRecord.objects.create(
            employee=emp,
            year=2020,
            month=3,
            salary=5
        )
        wage3 = WageRecord.objects.create(
            employee=emp,
            year=2015,
            month=2,
            salary=111
        )

        self.assertEqual(emp.get_year_salary(2020), 12350.0)
        self.assertEqual(emp.get_year_salary_with_tax(2020),
                         12350.0 * (1 - BackendProgrammer.TAX))

    @unittest.expectedFailure
    def test_year_salary_exception(self):
        emp = Employee.objects.create(
            id=666,
            employee_type=EmployeeConstants.BACKEND_PROGRAMMER,
            full_name="Another name"
        )
        emp.get_year_salary(2077)
