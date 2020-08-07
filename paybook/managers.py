from django.db import models

from paybook.constants import EmployeeConstants


class BackendProgrammerManager(models.Manager):
    def get_queryset(self):
        return super(BackendProgrammerManager, self).get_queryset().filter(
            employee_type=EmployeeConstants.BACKEND_PROGRAMMER
        )


class FreelanceCoderManager(models.Manager):
    def get_queryset(self):
        return super(FreelanceCoderManager, self).get_queryset().filter(
            employee_type=EmployeeConstants.FREELANCE_CODER
        )


class DesignerManager(models.Manager):
    def get_queryset(self):
        return super(DesignerManager, self).get_queryset().filter(
            employee_type=EmployeeConstants.DESIGNER
        )
