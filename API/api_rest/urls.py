from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    #Users URLs
    path('users/', views.get_users, name='get_users'),
    path('users/<str:name>', views.get_by_username, name='get_by_username'),
    path('users/data/', views.users_manager, name='users_manager'),
    
    #Products URLs
    path('products/', views.get_products, name='get_products'),
    path('products/<str:name>', views.get_by_productname, name='get_by_productname'),
    path('products/data/', views.products_manager, name='products_manager'),
]
