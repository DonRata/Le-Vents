
from django.shortcuts import render

# Create your views here.
def page_list(request):
    return render(request, 'LeVents/pagina_principal.html', {})

def productos_hombre(request):
    return render(request, 'LeVents/productos_hombre.html')