from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from .views import pagina_principal, listar_productos, producto_agregar, editar_producto, borrar_producto, producto_listado
from .views import ProductoListado, ProductoCreate, ProductoUpdate, ProductoDelete

from apps.usuario.views import quienes_somos

app_name = 'producto'  #nombre de la app, se usa para el redirect
urlpatterns = [
    path('', pagina_principal, name='pagina_principal'),
    path('quienes_somos/', quienes_somos, name='quienes_somos'),
    path('productos/<int:id_url>',listar_productos, name='product_list'),
    path('agregar/', login_required(producto_agregar), name='product_create'),
    path('productos_listado/', login_required(producto_listado), name='product_listado'),
    path('editar/<int:id_prod>/', login_required(editar_producto), name='product_edit'),
    path('eliminar/<int:id_prod>/', login_required(borrar_producto), name='product_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)