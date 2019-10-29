from django.contrib import admin
from .models import Usuario, Producto, Boleta, Venta
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(Venta)