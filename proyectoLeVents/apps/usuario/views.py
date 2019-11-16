from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView

from .models import Imagenes_Pagina
from .forms import RegistroForm

def quienes_somos(request):
	qsomos = Imagenes_Pagina.objects.all()
	return render(request, 'quienes_somos.html', {'qsomos': qsomos} )

def registro_exitoso(request):
	return render(request, 'usuario/registro_exitoso.html')
	

class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registro.html"
    form_class = RegistroForm
    success_url = '/accounts/registro_exitoso'
