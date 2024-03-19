from django.contrib import admin
from django.urls import path, include
from catalog.views import indexListView, contacts, ProductDetailView, add_product

urlpatterns = [
    path('', indexListView.as_view()),
    path('contacts/', contacts),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_url'),
    path('products/add/', add_product)
]