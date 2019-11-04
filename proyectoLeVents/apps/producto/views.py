from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#from django.contrib.auth.decorators import login_required
from .models import Categoria, Producto
from .forms import ProductoForm


def pagina_principal(request):
    categorias = Categoria.objects.all()
    return render(request, 'pagina_principal.html', {'categorias': categorias})

def producto_agregar(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/productos_listado/')
    else:
        form = ProductoForm()
    return render(request, 'producto/producto_agregar.html', {'form': form})

def producto_listado(request):
	producto = Producto.objects.all().order_by('id')
	return render(request, 'producto/productos_listado.html', {'producto':producto})

def listar_productos(request, id_url):
    #categorias = Categoria.objects.all().filter(id_categoria=id_categoria)
    if id_url:
        productos = Producto.objects.all().filter(categoria_id=id_url+1)
    return render(request, 'producto/productos_listar.html', {'productos': productos})


def editar_producto(request, id_prod):
    producto = Producto.objects.get(id_producto=id_prod)
    if request.method == "GET":
        form = ProductoForm(instance=producto)
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
        return redirect('/productos_listado/')
    return render(request, "producto/productos_editar.html", {'form': form})


def borrar_producto(request, id_prod):
    producto = Producto.objects.get(id_producto=id_prod)
    if request.method == 'POST':
        producto.delete()
        return redirect('/productos_listado/')
    return render(request, 'producto/producto_eliminar.html', {'producto': producto})

class ProductoListado(ListView):
    model = Producto
    template_name = 'producto/productos_listado.html'

class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_agregar.html'

class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/productos_editar.html'
    #success_url = reverse_lazy('/productos_listado/')