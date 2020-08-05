from django.db import models


class BackendProgrammerManager(models.Manager):
    def get_queryset(self):
        return super(BackendProgrammerManager, self).get_queryset().filter(
            employee_type="BE"
        )


class FreelanceCoderManager(models.Manager):
    def get_queryset(self):
        return super(FreelanceCoderManager, self).get_queryset().filter(
            employee_type="FR"
        )


class DesignerManager(models.Manager):
    def get_queryset(self):
        return super(DesignerManager, self).get_queryset().filter(
            employee_type="DSGN"
        )
