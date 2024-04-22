from main import views

from django.contrib import admin
from django.urls import path

from main.views import About, Contact

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('cart/', views.cart, name='cart'),
    ]