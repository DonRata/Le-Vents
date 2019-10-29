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

        def publish(self):
            self.save()
        
        def __str__(self):
            return self.run
        

