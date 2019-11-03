from django.shortcuts import render
from django.conf.urls import url, include
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Marca, Categoria, Tipo, Producto

def pagina_principal(request):
    categorias = Categoria.objects.all()
    return render(request, 'pagina_principal.html', {'categorias':categorias})

def quienes_somos(request):
    return render(request, 'quienes_somos.html', {})

def listar_productos(request, id_url):
    #categorias = Categoria.objects.all().filter(id_categoria=id_categoria)
    if(id_url):
        productos = Producto.objects.all().filter(categoria_id=id_url+1)
    return render(request, 'producto/productos_listar.html', {'productos':productos})