from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'department', 'mobile')


admin.site.register(User, UserAdmin)
