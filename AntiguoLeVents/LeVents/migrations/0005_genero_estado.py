# Generated by Django 2.2.6 on 2019-10-29 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeVents', '0004_auto_20191029_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='genero',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]