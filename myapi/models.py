# Create your models here.
# models.py
from django.db import models
class Wallet(models.Model):
    debtorId = models.IntegerField(unique=True)
    name = models.CharField(max_length=60)
    debtAmount = models.IntegerField()

    def __str__(self):
        return self.name
