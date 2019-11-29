from django.conf.urls import url
from django.urls import path, include
from .views import RegistroUsuario, quienes_somos, registro_exitoso
from django.contrib.auth.decorators import login_required

#Para la apis
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserViewSet, UserViewSetDetail

urlpatterns = [
    path('api/', UserViewSet.as_view()),
    path('api/<int:pk>/', UserViewSetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

app_name = 'usuario'
urlpatterns += [
    path('registrar/', RegistroUsuario.as_view()),
    path('registro_exitoso', registro_exitoso),
]
