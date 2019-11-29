from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

#Para importar el login_required y aplicarlo en el Crud
from django.contrib.auth.decorators import login_required

#Para importar las funciones que estan en views.py
from .views import pagina_principal, listar_productos, producto_agregar, editar_producto, borrar_producto, producto_listado
from .views import listar_marcas

#Para importar el quienes somos dinamico que esta en la app usuario
from apps.usuario.views import quienes_somos

#Para la apis
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductViewSet, ProductViewSetDetail

urlpatterns =[
    path('productos/api/', ProductViewSet.as_view()),
    path('productos/api/<int:pk>/', ProductViewSetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

app_name = 'producto'  #nombre de la app, se usa para el redirect
urlpatterns += [
    path('', pagina_principal, name='pagina_principal'),
    path('quienes_somos/', quienes_somos, name='quienes_somos'),
    path('productos/<int:id_url>/',listar_productos, name='product_list'),
    path('productos/<int:id_url>/marcas/<int:id_mrc>/',listar_marcas, name="brand_list"),
    path('agregar/', login_required(producto_agregar), name='product_create'),
    path('productos_listado/', login_required(producto_listado), name='product_listado'),
    path('editar/<int:id_prod>/', login_required(editar_producto), name='product_edit'),
    path('eliminar/<int:id_prod>/', login_required(borrar_producto), name='product_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)