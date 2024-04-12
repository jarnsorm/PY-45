from django.contrib import admin
from django.urls import path

from showcase import views

app_name = 'showcase'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('product/', views.product, name='product'),
]