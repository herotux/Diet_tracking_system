from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users.models import User

class Program(models.Model):
    class ProgramType(models.TextChoices):
        DIET = 'DIET', _('Diet')
        FITNESS = 'FITNESS', _('Fitness')

    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    program_type = models.CharField(_('program type'), max_length=50, choices=ProgramType.choices)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='programs_created', limit_choices_to={'role': User.Role.DOCTOR})
    patients = models.ManyToManyField(User, related_name='assigned_programs', limit_choices_to={'role': User.Role.PATIENT}, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'program'
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')

    def __str__(self):
        return self.name

class Task(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    day_of_week = models.IntegerField(_('day of week'), choices=[(i, _(str(i))) for i in range(1, 8)])

    class Meta:
        db_table = 'task'
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return self.name

class Progress(models.Model):
    class Status(models.TextChoices):
        COMPLETED = 'COMPLETED', _('Completed')
        PARTIALLY_COMPLETED = 'PARTIALLY_COMPLETED', _('Partially Completed')
        NOT_COMPLETED = 'NOT_COMPLETED', _('Not Completed')

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='progress')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress', limit_choices_to={'role': User.Role.PATIENT})
    status = models.CharField(_('status'), max_length=50, choices=Status.choices)
    note = models.TextField(_('note'), blank=True, null=True)
    date = models.DateField(_('date'), auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'progress'
        verbose_name = _('Progress')
        verbose_name_plural = _('Progresses')
        unique_together = ('task', 'patient', 'date')

    def __str__(self):
        return f"{self.patient.username} - {self.task.name} - {self.status}"