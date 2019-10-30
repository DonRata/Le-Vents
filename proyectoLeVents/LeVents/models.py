from django.db import models
from django.utils import timezone
from django import forms


class Usuario(models.Model):
    run = models.CharField(max_length=200)
    nombre_completo = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono_contacto = models.CharField(max_length=15)
    user = models.CharField(max_length=40)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_completo

class Imagenes_Pagina(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='imagenes pagina', null=True)
    
    def __str__(self):
        return self.nombre_completo

class Carousel(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='imagenes pagina', null=True)
    descripcion = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_completo

class Marca(models.Model):
    id_marca = models.IntegerField()
    nombre_marca = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_marca

#Genero corresponde a Categorias!!
class Genero(models.Model):
    id_genero = models.IntegerField()
    estado = models.BooleanField(default=True)
    nombre_genero = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='img/categorias', null=True)
    descripcion = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nombre_genero


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
    foto = models.ImageField(upload_to='img/productos', null=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto


class Boleta(models.Model):
    id_boleta = models.IntegerField()
    fecha_venta = models.DateField()

    def __str__(self):
        return self.id_boleta


class Venta(models.Model):
    id_venta = models.IntegerField()
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    comprador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_venta
