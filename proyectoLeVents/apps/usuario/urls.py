from django.conf.urls import url
from django.urls import path, include
from .views import RegistroUsuario, UserAPI, quienes_somos

app_name = 'usuario'
urlpatterns = [
    path('registrar/', RegistroUsuario.as_view()),
    url(r'^api', UserAPI.as_view(), name="api"),

]
