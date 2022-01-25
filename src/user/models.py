from django.db import models
from django.contrib.auth.models import AbstractUser
from department.models import Department


class User(AbstractUser):
    ROLE = {
        ('1', 'normal user'),
        ('2', 'operator user'),
    }
    role = models.CharField(max_length=1, choices=ROLE)
    mobile = models.CharField(max_length=13)
    department = models.ForeignKey(Department, default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name="department")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
