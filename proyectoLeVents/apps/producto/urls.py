from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from . import views
#from apps.producto.views import pagina_principal 

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('productos/<int:id_url>', views.listar_productos, name='product_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)