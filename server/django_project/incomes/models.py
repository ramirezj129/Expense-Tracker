from django.db import models

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, unique=True, default='')

    def __str__(self):
        return f"Income: {self.amount} - {self.description}"
