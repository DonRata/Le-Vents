from rest_framework.serializers import ModelSerializer

from .models import Producto 


class ProductSerializer(ModelSerializer):

	class Meta:
		model = Producto
		fields = '__all__'
