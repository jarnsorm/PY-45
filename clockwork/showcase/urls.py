from django.urls import path
from showcase.views import Catalog, Collection, Product, About, Contact, Brand

app_name = 'showcase'

urlpatterns = [
    path('', Catalog.as_view(), name='catalog'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('collection/<slug:col_slug>/', Collection.as_view(), name='collection'),
    path('brand/<slug:brand_slug>/', Brand.as_view(), name='brand'),
    path('product/<slug:p_slug>/', Product.as_view(), name='product'),
]