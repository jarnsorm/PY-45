from django.urls import path
from .views import register, login_view, account, select_view, logout_view

app_name = 'accounts'

urlpatterns = [
    path('', select_view, name='select'),
    path('profile/', account, name='account'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

]