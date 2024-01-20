from .models import Client, Bill, Product, BillProduct
from rest_framework import permissions, viewsets
from facturacion.serializers import ClientSerializer, BillSerializer, ProductSerializer, BillProductSerializer
from rest_framework.authentication import TokenAuthentication




# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]    
    

class BillProductViewSet(viewsets.ModelViewSet):
    queryset = BillProduct.objects.all()
    serializer_class = BillProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]    
    
    
