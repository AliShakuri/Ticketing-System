from django.contrib import admin
from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date')


admin.site.register(Department, DepartmentAdmin)
