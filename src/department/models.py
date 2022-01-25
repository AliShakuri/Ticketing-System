from django.db import models


class Department(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
