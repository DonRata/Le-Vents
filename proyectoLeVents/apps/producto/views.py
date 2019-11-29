from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Categoria, Producto, Marca
from .forms import ProductoForm

#Para importar las apis
from rest_framework import generics
from .serializers import ProductSerializer

class ProductViewSet(generics.ListCreateAPIView):
        queryset= Producto.objects.all()
        serializer_class= ProductSerializer

class ProductViewSetDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset= Producto.objects.all()
        serializer_class= ProductSerializer


def pagina_principal(request):
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    return render(request, 'pagina_principal.html', {'categorias': categorias,'marcas':marcas })

def categorias_desplegadas(request):
    marcas = Marca.objects.all()
    return render(request, 'base/footer.html', {'marcas':marcas})

def producto_agregar(request):
    user = request.user
    if user.has_perm('producto.moderador'):
        if request.method == 'POST':
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return redirect('/productos_listado/')
        else:
            form = ProductoForm()
        return render(request, 'producto/producto_agregar.html', {'form': form})
    else:
        return redirect('/')

def producto_listado(request):
    productos = Producto.objects.all().order_by('id')
    user = request.user
    if user.has_perm('producto.moderador'):
        return render(request, 'producto/productos_listado.html', {'productos':productos})
    else:
        return redirect('/') 

def listar_productos(request, id_url):
    # categorias = Categoria.objects.all().filter(id_categoria=id_categoria)
    marcas = Marca.objects.all()
    if id_url==1:
        productos = Producto.objects.all().filter(categoria_id=id_url+1)
        contexto = 'producto/productos_listar.html'
    if id_url==2:
        productos = Producto.objects.all().filter(categoria_id=id_url+1)
        contexto = 'producto/productos_listar_mujer.html'
    return render(request, contexto, {'productos': productos,'marcas':marcas})

def listar_marcas(request, id_url, id_mrc):
    # categorias = Categoria.objects.all().filter(id_categoria=id_categoria)
    if id_url==1:
        productos = Producto.objects.all().filter(categoria_id=2, marca_id=id_mrc)
        marcas = Marca.objects.all()
        contexto = 'producto/productos_listar.html'
    if id_url==2:
        productos = Producto.objects.all().filter(categoria_id=3, marca_id=id_mrc)
        marcas = Marca.objects.all()
        contexto = 'producto/productos_listar_mujer.html'
    return render(request, contexto, {'productos': productos,'marcas':marcas})
    

def editar_producto(request, id_prod):
    producto = Producto.objects.get(id_producto=id_prod)
    user = request.user
    if user.has_perm('producto.moderador'):
        if request.method == "GET":
            form = ProductoForm(instance=producto)
        else:
            form = ProductoForm(request.POST, request.FILES,instance=producto)
            if form.is_valid():
                producto = form.save(commit=False)
                producto.save()
            return redirect('/productos_listado/')
        return render(request, "producto/productos_editar.html", {'form': form})
    else:
        return redirect('/') 


def borrar_producto(request, id_prod):
    producto = Producto.objects.get(id_producto=id_prod)
    user = request.user
    if user.has_perm('producto.moderador'):
        if request.method == 'POST':
            producto.delete()
            return redirect('/productos_listado/')
        return render(request, 'producto/producto_eliminar.html', {'producto': producto})
    else:
        return redirect('/') 


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
