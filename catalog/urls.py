from django.contrib import admin
from django.urls import path, include
from catalog.views import indexListView, ProductDetailView, contactsPageView, ProductAddView, ProductUpdateView

urlpatterns = [
    path('', indexListView.as_view(), name='index'),
    path('contacts/', contactsPageView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/add/', ProductAddView.as_view(), name='product_add')
]