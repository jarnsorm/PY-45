from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf.models import DRFCart, CartItem
from drf.permissions import IsAdminOrReadOnly
from drf.serializers import ProductsSerializer, CartSerializer, AddCartItemSerializer
from showcase.models import Products


class ProductsAPIViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name', 'price', 'category', 'brand']
    ordering = ['name']
    filterset_fields = ['category', 'brand']
    permission_classes = (IsAdminOrReadOnly,)


# class ProductsListView(generics.ListAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     ordering_fields = ['name', 'price', 'category', 'brand']
#     ordering = ['name']
#
#     filterset_fields = ['category', 'brand']


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, created = DRFCart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart, created = DRFCart.objects.get_or_create(user=request.user)
        serializer = AddCartItemSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.validated_data['product']
            quantity = serializer.validated_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': quantity})
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            return Response({'status': 'item added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)