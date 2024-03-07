from django.contrib import admin
from django.urls import path, include
from catalog.views import index, contacts, one_product, add_product

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('products/<int:pk>', one_product, name='product_url'),
    path('products/add/', add_product)
]