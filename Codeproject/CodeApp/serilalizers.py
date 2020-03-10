from rest_framework.serializers import ModelSerializer
from .models import Products,Companies

class ProductSerilaizer(ModelSerializer):
    class Meta:
        model=Products
        fields ='__all__'


class CompanySerilaizer(ModelSerializer):
    class Meta:
        model=Companies
        fields = '__all__'