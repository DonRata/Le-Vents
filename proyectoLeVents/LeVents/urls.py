from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from LeVents.views import ProductoList, ProductoUpdate
from LeVents.views import editar_producto, productos_hombre

urlpatterns = [   
    path('', views.pagina_principal),
    path('productos-hombre/', views.productos_hombre ),
    #url(r'^productos_hombre/', producto_list, name="producto_listar"),
    path('productos_mujer', views.productos_mujer ),
    url(r'^productos_editar/(?P<id_producto>\d+)/$', editar_producto, name='producto_editar'),
    path('quienes-somos', views.quienes_somos ),
    path('registrar_usuario', views.registrar_usuario),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
