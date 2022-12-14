# Generated by Django 4.1 on 2022-09-02 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0008_rename_customer_id_cuenta_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='account_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.tipocuenta'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='address_type_required',
            field=models.ForeignKey(blank=True, db_column='address_type_required', null=True, on_delete=django.db.models.deletion.CASCADE, to='cuentas.direccioncliente'),
        ),
    ]
