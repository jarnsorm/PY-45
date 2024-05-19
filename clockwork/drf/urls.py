from rest_framework import routers
from django.urls import path, include
from drf.views import ProductsAPIViewset, CartView, AddToCartView

app_name = 'drf'

router = routers.DefaultRouter()
router.register(r'products', ProductsAPIViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add_to_cart'),
    path('drf-auth/', include('rest_framework.urls')),
    # path('products/', ProductsListView.as_view(), name='product-list'),
    ]