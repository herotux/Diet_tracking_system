from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Role(models.TextChoices):
        DOCTOR = 'DOCTOR', _('Doctor')
        PATIENT = 'PATIENT', _('Patient')
        ADMIN = 'ADMIN', _('Admin')

    role = models.CharField(_('role'), max_length=50, choices=Role.choices, default=Role.PATIENT)

    class Meta:
        db_table = 'user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username