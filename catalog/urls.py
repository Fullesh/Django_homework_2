from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page

from catalog.views import indexListView, ProductDetailView, contactsPageView,\
    ProductAddView, ProductUpdateView, ProudctDeleteView

urlpatterns = [
    path('', indexListView.as_view(), name='index'),
    path('contacts/', contactsPageView.as_view()),
    path('products/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('products/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/add/', ProductAddView.as_view(), name='product_add'),
    path('products/delete/<int:pk>/', ProudctDeleteView.as_view(), name='product_delete')
]
