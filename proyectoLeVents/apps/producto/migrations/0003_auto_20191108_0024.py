# Generated by Django 2.2.6 on 2019-11-08 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_auto_20191104_1220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'permissions': (('moderador', 'Es moderador'), ('usuario', 'Es usuario'))},
        ),
    ]
