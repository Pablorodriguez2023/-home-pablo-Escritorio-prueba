from .models import Client, Bill, Product, BillProduct
from rest_framework import serializers



class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'document', 'first_name', 'last_name', 'email']


class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'client_id', 'company_name', 'nit', 'code']
        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'attribute']
        
class BillProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BillProduct
        fields = ['id', 'bill_id', 'product_id']
        
