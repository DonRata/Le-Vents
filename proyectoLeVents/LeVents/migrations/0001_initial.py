# Generated by Django 2.2.6 on 2019-10-29 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_boleta', models.IntegerField()),
                ('fecha_venta', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_genero', models.IntegerField()),
                ('nombre_genero', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_marca', models.IntegerField()),
                ('nombre_marca', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_producto', models.IntegerField()),
                ('nombre_producto', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('foto', models.ImageField(upload_to='img')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LeVents.Genero')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LeVents.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tipo', models.IntegerField()),
                ('nombre_tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=200)),
                ('nombre_completo', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono_contacto', models.CharField(max_length=15)),
                ('user', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_venta', models.IntegerField()),
                ('boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LeVents.Boleta')),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LeVents.Usuario')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LeVents.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LeVents.Tipo'),
        ),
    ]
