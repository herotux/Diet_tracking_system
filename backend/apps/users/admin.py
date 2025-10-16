from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    # Fields to display in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')
    list_filter = ('role', 'is_staff', 'is_superuser', 'groups')

    # Fields to display in the detail/edit view
    fieldsets = UserAdmin.fieldsets + (
        ('Role & Profile', {
            'fields': (
                'role', 'national_id', 'birth_date', 'gender', 'phone_number', 'address',
            ),
        }),
        ('Patient Info', {
            'fields': (
                'height_cm', 'weight_kg', 'activity_level', 'goal',
            ),
        }),
        ('Doctor Info', {
            'fields': (
                'specialty', 'license_number', 'clinic_address',
            ),
        }),
    )

    # Fields for the add user form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': (
                'role', 'first_name', 'last_name', 'email',
            ),
        }),
    )