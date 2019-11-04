from django.conf.urls import url
from django.urls import path, include
from .views import RegistroUsuario, UserAPI, quienes_somos

app_name = 'usuario'
urlpatterns = [
    #path('quienes_somos/', quienes_somos, name='quienes_somos'),
    url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
    url(r'^api', UserAPI.as_view(), name="api"),

]
