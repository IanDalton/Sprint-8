# Generated by Django 4.1.1 on 2022-09-10 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0012_alter_cliente_customer_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion',
            name='customer_id',
            field=models.ForeignKey(blank=True, db_column='cliente_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='cuentas.cliente'),
        ),
    ]
