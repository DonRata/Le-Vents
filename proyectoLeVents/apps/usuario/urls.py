from django.conf.urls import url
from django.urls import path, include
from .views import RegistroUsuario, UserAPI, quienes_somos, registro_exitoso
from django.contrib.auth.decorators import login_required

app_name = 'usuario'
urlpatterns = [
    path('registrar/', login_required(RegistroUsuario.as_view())),
    path('registro_exitoso', registro_exitoso),
    url(r'^api', UserAPI.as_view(), name="api"),

]
