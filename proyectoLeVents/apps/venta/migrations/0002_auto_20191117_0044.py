# Generated by Django 2.2.6 on 2019-11-17 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='comprador',
            field=models.CharField(max_length=250),
        ),
    ]
