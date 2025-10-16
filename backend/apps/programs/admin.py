from django.contrib import admin
from .models import Program, Task, Progress

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'program_type', 'doctor', 'created_at')
    list_filter = ('program_type', 'doctor')
    search_fields = ('name', 'description')
    filter_horizontal = ('patients',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'program', 'day_of_week')
    list_filter = ('program', 'day_of_week')
    search_fields = ('name', 'description')

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('patient', 'task', 'status', 'date')
    list_filter = ('status', 'date', 'patient')
    search_fields = ('patient__username', 'task__name')