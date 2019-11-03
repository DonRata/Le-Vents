from django.forms import ModelForm
from .models import Categoria, Producto
from django import forms

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'id_producto',
            'estado',
            'nombre_producto',
            'precio',
            'stock',
            'foto',
            'marca',
            'categoria',
            'tipo'
        ]
        labels = {
            'id_producto': 'Id Producto',
            'estado': 'Estado',
            'nombre_producto': 'Nombre',
            'precio' : 'Precio',
            'stock': 'Stock',
            'foto' : 'Imagen',
            'marca': 'Marca',
            'categoria': 'Categoria',
            'tipo': 'Tipo',
        }
        widgets = {
            'id_producto': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_producto': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'stock': forms.TextInput(attrs={'class':'form-control'}),
            'marca': forms.Select(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class':'form-control'}),
        }