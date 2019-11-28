from rest_framework.serializers import ModelSerializer

from .models import Producto 


class ProductSerializer(ModelSerializer):

	class Meta:
		model = Producto
		fields = ('id_producto', 'nombre_producto', 'precio', 'marca')
