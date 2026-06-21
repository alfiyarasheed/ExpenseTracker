from django.db import models

# Create your models here.
class Expense(models.Model):
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.CharField(max_length=50)
    description=models.CharField(max_length=255)
    expense_date=models.DateField()

    def __str__(self):
        return self.category
