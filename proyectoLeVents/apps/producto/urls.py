from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from .views import pagina_principal, listar_productos
from .views import ProductoListado, ProductoCreate, ProductoUpdate, ProductoDelete
from apps.usuario.views import quienes_somos
#from apps.producto.views import pagina_principal 

app_name = 'producto'  #nombre de la app, se usa para el redirect
urlpatterns = [
    path('', pagina_principal, name='pagina_principal'),
    path('quienes_somos/', quienes_somos, name='quienes_somos'),
    path('productos/<int:id_url>',listar_productos, name='product_list'),
    path('agregar/', login_required(ProductoCreate.as_view()), name='product_create'),
    path('productos_listado/', login_required(ProductoListado.as_view()), name='product_listado'),
    re_path(r'^editar/(?P<pk>\d+)/$', login_required(ProductoUpdate.as_view()), name='product_edit'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', login_required(ProductoDelete.as_view()), name='product_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)