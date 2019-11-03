from django.shortcuts import render, redirect, reverse
from django.conf.urls import url, include
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Marca, Categoria, Tipo, Producto
from .forms import ProductoForm

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

def editar_producto(request, id_prod):
    producto = Producto.objects.get(id_producto=id_prod)
    if request.method == "GET":
        form= ProductoForm(instance=producto)
    else:
        form= ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
    return render(request, "producto/productos_editar.html", {'form':form})

def borrar_producto(request, id_prod):
	producto = Producto.objects.get(id_producto=id_prod)
	if request.method == 'POST':
		producto.delete()
	return render(request, 'producto/producto_eliminar.html', {'producto':producto})