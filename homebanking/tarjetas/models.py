from django.db import models
from cuentas.models import Cliente

# Create your models here.


class MarcasTarjeta(models.Model):
    brand_id = models.TextField(primary_key=True, blank=True)
    type_brand = models.TextField()

    class Meta:
        managed = True
        db_table = 'marcas_tarjeta'



class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True, blank=True)
    card_number = models.TextField(unique=True, blank=True, null=True)
    card_cvv = models.IntegerField()
    card_gived = models.TextField(blank=True, null=True)
    card_expiration = models.TextField(blank=True, null=True)
    card_type = models.TextField(blank=True, null=True)
    card_brand = models.ForeignKey('MarcasTarjeta', models.DO_NOTHING, db_column='card_brand', blank=True, null=True)
    client = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='client', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tarjeta'

