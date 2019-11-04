from django.db import models
from django.utils import timezone
from django import forms


class Marca(models.Model):
    id_marca = models.IntegerField()
    nombre_marca = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_marca

class Categoria(models.Model):
    id_categoria = models.IntegerField()
    estado = models.BooleanField(default=True)
    nombre_categoria = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='img/categorias', null=True)
    descripcion = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nombre_categoria

class Tipo(models.Model):
    id_tipo = models.IntegerField()
    nombre_tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_tipo


class Producto(models.Model):
    id_producto = models.IntegerField()
    estado = models.BooleanField(default=True)
    nombre_producto = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    foto = models.ImageField(upload_to='img/productos', null=True, blank= True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto