from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LeVents.urls')),
    path('productos_hombre', include('LeVents.urls')),
    path('productos_mujer', include('LeVents.urls')),
    path('quienes_somos', include('LeVents.urls')),
    path('registrar_usuario', include('LeVents.urls')),
]
