from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [   
    path('', views.pagina_principal),
    path('productos-hombre', views.productos_hombre ),
    path('productos-mujer', views.productos_mujer ),
    path('quienes-somos', views.quienes_somos ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
