from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product, Customer, Comment
from .serializers import ProductSerializer, ProductListSerializer, CustomerSerializer, CommentSerializer, CommentListSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductListSerializer(queryset, many=True)
        return Response(serializer.data)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentListSerializer(queryset, many=True)
        return Response(serializer.data)
