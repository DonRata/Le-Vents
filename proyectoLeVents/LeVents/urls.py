from django.urls import path, include
from . import views

urlpatterns = [   
    path('', views.page_list),
    path('productos-hombre', views.productos_hombre ),
]
