from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from . import views
from apps.usuario.views import quienes_somos
#from apps.producto.views import pagina_principal 

app_name = 'producto'  #nombre de la app, se usa para el redirect
urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('quienes_somos/', quienes_somos, name='quienes_somos'),
    path('productos/<int:id_url>', views.listar_productos, name='product_list'),
    path('editar/<int:id_prod>', views.editar_producto, name='product_edit'),
    path('eliminar/<int:id_prod>', views.borrar_producto, name='product_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)