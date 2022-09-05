from logging import PlaceHolder
from django.db import models
from cuentas.models import Cliente

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.CharField(max_length=255)
    loan_date = models.DateField(max_length=9)
    loan_total = models.FloatField()
    customer_id = models.ForeignKey(Cliente, models.CASCADE)

