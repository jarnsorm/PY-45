from django.urls import path

from main.views import search_view

app_name = 'main'

urlpatterns = [
    path('', search_view, name='search'),
    ]