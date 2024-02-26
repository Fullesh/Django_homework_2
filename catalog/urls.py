from django.contrib import admin
from django.urls import path, include
from catalog.views import index, contacts

urlpatterns = [
    path('', index),
    path('contacts/', contacts)
]