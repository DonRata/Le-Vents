from django.db import models
from django.utils import timezone
from django import forms



class Post(models.Model):
        author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
            default=timezone.now)
        published_date = models.DateTimeField(
            blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title

class Usuario(models.Model):
        run = models.CharField(max_length=200 )
        nombre = models.CharField(max_length=40)
        apellido_paterno = models.CharField(max_length=40)
        apellido_materno = models.CharField(max_length=40)
        user = models.CharField(max_length=40)
        password = models.CharField(max_length=50)

        def publish(self):
            self.save()
        
        def __str__(self):
            return self.run
        
        
