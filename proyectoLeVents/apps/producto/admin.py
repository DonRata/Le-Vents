from django.contrib import admin
from .models import Marca, Categoria, Tipo, Producto

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Tipo)
admin.site.register(Producto)