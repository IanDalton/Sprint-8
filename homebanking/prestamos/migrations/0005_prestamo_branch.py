# Generated by Django 4.1.1 on 2022-09-08 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0012_alter_cliente_customer_username'),
        ('prestamos', '0004_alter_prestamo_options_alter_prestamo_loan_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cuentas.sucursal'),
        ),
    ]
