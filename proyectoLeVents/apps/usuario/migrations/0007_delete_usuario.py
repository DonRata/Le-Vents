# Generated by Django 2.2.6 on 2019-11-17 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0002_auto_20191117_0044'),
        ('usuario', '0006_auto_20191107_2314'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
