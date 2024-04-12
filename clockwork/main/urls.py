from main import views

from django.contrib import admin
from django.urls import path

from clockwork import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about_us, name='about'),
    path('contacts/', views.contact_us, name='contacts'),
    path('cart/', views.cart, name='cart'),
    ]