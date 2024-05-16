from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from drf.serializers import ProductsSerializer
from showcase.models import Products, Categories


class ProductsAPIView(APIView):
    def get(self, request):
        lst = Products.objects.all().values()
        return Response({'products': list(lst)})

    def post(self, request):
        new_product = Products.objects.create(
            name=request.data['name'],
            slug=request.data['slug'],
            brand=request.data['brand'],
            description=request.data['description'],
            price=request.data['price'],
            category=Categories.objects.get(id=request.data['category']),
        )
        return Response({'product': model_to_dict(new_product)})