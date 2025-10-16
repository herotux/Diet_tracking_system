from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('program_type', models.CharField(choices=[('DIET', 'Diet'), ('FITNESS', 'Fitness')], max_length=50, verbose_name='program type')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs_created', to=settings.AUTH_USER_MODEL)),
                ('patients', models.ManyToManyField(blank=True, limit_choices_to={'role': 'PATIENT'}, related_name='assigned_programs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programs',
                'db_table': 'program',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('day_of_week', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], verbose_name='day of week')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='programs.program')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('COMPLETED', 'Completed'), ('PARTIALLY_COMPLETED', 'Partially Completed'), ('NOT_COMPLETED', 'Not Completed')], max_length=50, verbose_name='status')),
                ('note', models.TextField(blank=True, null=True, verbose_name='note')),
                ('date', models.DateField(auto_now_add=True, verbose_name='date')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(limit_choices_to={'role': 'PATIENT'}, on_delete=django.db.models.deletion.CASCADE, related_name='progress', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='programs.task')),
            ],
            options={
                'verbose_name': 'Progress',
                'verbose_name_plural': 'Progresses',
                'db_table': 'progress',
                'unique_together': {('task', 'patient', 'date')},
            },
        ),
    ]