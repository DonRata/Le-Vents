from django.db import models
from django.utils import timezone
from django import forms
from apps.producto.models import Producto
from apps.usuario.models import Usuario

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
