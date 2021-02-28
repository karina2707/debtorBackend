# Create your models here.
# models.py
from django.db import models
class Wallet(models.Model):
    debtorId = models.IntegerField("id", primary_key=True, unique=True)
    name = models.CharField("name", max_length=60)
    debtAmount = models.IntegerField("Debt amount")

    def __str__(self):
        return self.name
