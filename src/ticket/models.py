from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from department.models import Department

# Ticket model
class Ticket(models.Model):
    title = models.CharField(max_length=50)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL, related_name='tickets')
    person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True, related_name='user')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='ticket')
    text = models.TextField()
    posted = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.person.username} - {self.title}"
