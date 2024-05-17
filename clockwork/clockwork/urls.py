"""
URL configuration for clockwork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, URLResolver
from django.conf import settings
from django.conf.urls.static import static

from drf.views import ProductsAPIList, ProductsAPIUpdate, ProductsAPICRUD, ProductsAPIRetrieve

urlpatterns: list[URLResolver] = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', ProductsAPIList.as_view()),
    path('api/v1/product/<int:pk>/', ProductsAPIRetrieve.as_view()),
    path('api/v1/product/update/<int:pk>/', ProductsAPIUpdate.as_view()),
    path('api/v1/product/crud/<int:pk>/', ProductsAPICRUD.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('search/', include('main.urls')),
    path('', include('showcase.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)