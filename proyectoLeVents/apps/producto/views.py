from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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
    success_url = '/productos_listado/'

class ProductoDelete(DeleteView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_eliminar.html'
    success_url = '/productos_listado/'
