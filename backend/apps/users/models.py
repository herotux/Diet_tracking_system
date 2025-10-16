from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Role(models.TextChoices):
        PATIENT = 'PATIENT', _('Patient')
        DOCTOR = 'DOCTOR', _('Doctor')
        ADMIN = 'ADMIN', _('Admin')

    role = models.CharField(_('role'), max_length=10, choices=Role.choices, default=Role.PATIENT)

    # Common Information
    national_id = models.CharField(_("national id"), max_length=10, unique=True, blank=True, null=True)
    birth_date = models.DateField(_("birth date"), blank=True, null=True)

    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')

    gender = models.CharField(_("gender"), max_length=1, choices=Gender.choices, blank=True, null=True)
    phone_number = models.CharField(_("phone number"), max_length=15, blank=True, null=True)
    address = models.TextField(_("address"), blank=True, null=True)

    # Patient-specific fields
    height_cm = models.PositiveIntegerField(_("height (cm)"), validators=[MinValueValidator(50), MaxValueValidator(250)], blank=True, null=True)
    weight_kg = models.PositiveIntegerField(_("weight (kg)"), validators=[MinValueValidator(20), MaxValueValidator(300)], blank=True, null=True)

    class ActivityLevel(models.TextChoices):
        SEDENTARY = 'sedentary', _('Sedentary')
        LIGHT = 'light', _('Lightly active')
        MODERATE = 'moderate', _('Moderately active')
        ACTIVE = 'active', _('Active')
        VERY_ACTIVE = 'very_active', _('Very active')

    activity_level = models.CharField(_("activity level"), max_length=20, choices=ActivityLevel.choices, blank=True, null=True)

    class Goal(models.TextChoices):
        WEIGHT_LOSS = 'weight_loss', _('Weight Loss')
        WEIGHT_GAIN = 'weight_gain', _('Weight Gain')
        MAINTENANCE = 'maintenance', _('Maintenance')
        FITNESS = 'fitness', _('Fitness')

    goal = models.CharField(_("goal"), max_length=20, choices=Goal.choices, blank=True, null=True)

    # Doctor-specific fields
    specialty = models.CharField(_("specialty"), max_length=100, blank=True, null=True)
    license_number = models.CharField(_("license number"), max_length=50, blank=True, null=True)
    clinic_address = models.TextField(_("clinic address"), blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username}) - {self.get_role_display()}"