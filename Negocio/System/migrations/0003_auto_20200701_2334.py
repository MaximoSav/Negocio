# Generated by Django 2.2 on 2020-07-01 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0002_auto_20200701_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='descuento',
            field=models.BooleanField(),
        ),
    ]