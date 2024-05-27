from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Set a default value

    def __str__(self):
        return f"Income - {self.amount}"
