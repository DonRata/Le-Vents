from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# -----------  para nuestos modelos --------------------
from .models import Usuario, Marca, Genero, Tipo, Producto, Boleta, Venta, Imagenes_Pagina
from .forms import ProductoForm

def pagina_principal(request):
    generos = Genero.objects.all()
    return render(request, 'LeVents/pagina_principal.html', {'generos': generos})


def productos_hombre(request):
    productos = Producto.objects.all().filter(genero_id=1)
    return render(request, "LeVents/productos_hombre.html", {'productos': productos})


def productos_mujer(request):
    productos = Producto.objects.all().filter(genero_id=2)
    return render(request, 'LeVents/productos_mujer.html', {'productos': productos})

def quienes_somos(request):
    return render(request, 'LeVents/quienes_somos.html', {})

def mostrar_producto(request, id_producto):
    instancia = Producto.objects.get(id_producto=id_producto)
    form= ProductoForm(instance=instancia)
    if request.method == "POST":
        form= ProductoForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "LeVents/producto.html", {'form':form})
