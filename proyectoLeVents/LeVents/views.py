
from django.shortcuts import render

# Create your views here.
def page_list(request):
    return render(request, 'LeVents/pagina_principal.html', {})

def productos_hombre(request):
	productos = Productos.objects.get(id_genero=1)

    return render(request, 'LeVents/productos_hombre.html', {'productos': productos})

def productos_mujer(request):
    return render(request, 'LeVents/productos_mujer.html', {})

def quienes_somos(request):
    return render(request, 'LeVents/quienes_somos.html', {})