from django.forms import ModelForm
from .models import Usuario, Genero, Producto
from django import forms

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['id_genero', 'estado', 'nombre_genero', 'imagen', 'descripcion']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto','estado','nombre_producto','precio','stock','foto','marca','genero','tipo']

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['run','nombre_completo','email','fecha_nacimiento','telefono_contacto','user','password','password']