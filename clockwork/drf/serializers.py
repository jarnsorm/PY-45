from rest_framework import serializers
from showcase.models import Products
from .models import DRFCart, CartItem


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = DRFCart
        fields = ['user', 'items']


class AddCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']
