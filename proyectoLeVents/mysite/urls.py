from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.conf.urls import url, include
from django.urls import path, include

app_name = "users"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LeVents.urls')),
    path('productos_hombre', include('LeVents.urls')),
    path('producto_list', include('LeVents.urls')),
    path('productos_mujer', include('LeVents.urls')),
    path('quienes_somos', include('LeVents.urls')),
    path('login/', LoginView.as_view(template_name='LeVents/login.html'), name ="login"),
]
