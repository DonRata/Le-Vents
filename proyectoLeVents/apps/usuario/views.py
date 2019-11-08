import json
from django.shortcuts import render
from rest_framework.views import APIView

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Imagenes_Pagina
from .forms import RegistroForm
from .serializers import UserSerializer

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


class UserAPI(APIView):
	serializer = UserSerializer

	def get(self, request, format=None):
		lista = User.objects.all()
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')
