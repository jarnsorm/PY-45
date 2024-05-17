from rest_framework import generics
from drf.serializers import ProductsSerializer
from showcase.models import Products


# апишечка для просмотра всех товаров и добавления новых
class ProductsAPIList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


# апишечка для просмотра товара по id
class ProductsAPIRetrieve(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


# апишечка для обновления товара по id
class ProductsAPIUpdate(generics.UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


# апишечка для просмотра, изменения и удаления товара по id
class ProductsAPICRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
