from django.contrib import admin
from .models import Usuario, Marca, Genero, Tipo, Producto, Boleta, Venta
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Marca)
admin.site.register(Genero)
admin.site.register(Tipo)
admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(Venta)