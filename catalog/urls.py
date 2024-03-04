from django.contrib import admin
from django.urls import path, include
from catalog.views import index, contacts, products

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('products/', products)
]