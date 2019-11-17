from django.db import models
from django.utils import timezone
from django import forms
from django.utils.translation import ugettext as _

class Imagenes_Pagina(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='imagenes pagina', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='imagenes pagina', null=True, blank=True)
    descripcion = models.TextField(default=' ')
    
    def __str__(self):
        return self.nombre
