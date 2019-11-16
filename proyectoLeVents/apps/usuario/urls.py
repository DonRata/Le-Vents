from django.conf.urls import url
from django.urls import path, include
from .views import RegistroUsuario, quienes_somos, registro_exitoso
from django.contrib.auth.decorators import login_required

app_name = 'usuario'
urlpatterns = [
    path('registrar/', RegistroUsuario.as_view()),
    path('registro_exitoso', registro_exitoso),
]
