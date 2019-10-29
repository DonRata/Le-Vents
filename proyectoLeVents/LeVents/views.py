from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# -----------  para nuestos modelos --------------------
from .models import Usuario, Marca, Genero, Tipo, Producto, Boleta, Venta


def page_list(request):
    return render(request, 'LeVents/pagina_principal.html', {})


def productos_hombre(request):
    productos = Producto.objects.all()
    return render(request, "LeVents/productos_hombre.html", {'productos': productos})


def productos_mujer(request):
    return render(request, 'LeVents/productos_mujer.html', {})

def quienes_somos(request):
    return render(request, 'LeVents/quienes_somos.html', {})
