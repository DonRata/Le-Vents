from django.db import models
from django.utils import timezone
from django import forms

class Usuario(models.Model):
        run = models.CharField(max_length=200 )
        nombre_completo = models.CharField(max_length=200)
        email = models.CharField(max_length=100)
        fecha_nacimiento = models.DateField()
        telefono_contacto = models.CharField(max_length=15)
        user = models.CharField(max_length=40)
        password = models.CharField(max_length=50)

        def str(self):
            return self.run

class Producto(models.Model):
        idProducto = models.IntegerField()
        nombre = models.CharField(max_length=100)
        precio = models.IntegerField()
        stock = models.IntegerField()
        foto = models.ImageField()

        def str(self):
            return self.idProducto

class Boleta(models.Model):
        idBoleta = models.IntegerField()
        fecha_venta = models.DateField()

        def str(self):
            return self.idBoleta


class Venta(models.Model):
        idVenta = models.IntegerField()
        boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
        comprador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
        producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

        def str(self):
            return self.idVenta
        

