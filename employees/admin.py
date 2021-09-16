"""Employees admin classes"""
#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#Models
from django.contrib.auth.models import User
from employees.models import Employees

# Register your models here.
@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    pass

class EmployeeInline(admin.StackedInline):
    """Employee in-line admin for users."""
    model = Employees
    can_delete = False
    verbose_name_plural = 'employees'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (EmployeeInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)