from rest_framework import serializers
from .models import Product, Customer, Comment

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentListSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = ['comment', 'customer']

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
