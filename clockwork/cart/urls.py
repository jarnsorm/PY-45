from django.urls import path
from .views import CartRemoveView, CartDetailView, CartAddAjaxView, update_cart

app_name = 'cart'


urlpatterns = [
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('add/', CartAddAjaxView.as_view(), name='add_to_cart_ajax'),
    path('remove/<int:product_id>/', CartRemoveView.as_view(), name='cart_remove'),
    path('update_cart/', update_cart, name='update_cart'),
]