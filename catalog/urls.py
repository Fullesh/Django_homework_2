from django.contrib import admin
from django.urls import path, include
from catalog.views import indexListView, ProductDetailView, contactsPageView, ProductAddView

urlpatterns = [
    path('', indexListView.as_view()),
    path('contacts/', contactsPageView.as_view(), name='contacts'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_url'),
    path('products/add/', ProductAddView.as_view(), name='add_product')
]