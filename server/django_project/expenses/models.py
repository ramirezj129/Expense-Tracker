from django.db import models
from django.contrib.auth.models import User

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.category}: {self.amount}"
