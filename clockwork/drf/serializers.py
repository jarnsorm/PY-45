from rest_framework import serializers

from showcase.models import Products


class ProductsSerializer(serializers.Serializer):
    class Meta:
        name = serializers.CharField(max_length=100)
        slug = serializers.SlugField(max_length=200,)
        brand = serializers.CharField(max_length=20)
        description = serializers.CharField()
        price = serializers.DecimalField(max_digits=8, decimal_places=2, default=0.00)
        category = serializers.ImageField()