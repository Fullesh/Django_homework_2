from django.contrib import admin
from django.urls import path, include
from blog.apps import BlogConfig
from blog.views import BlogRecordCreate, BlogIndexView

app_name = BlogConfig.name


urlpatterns = [
    path('create/', BlogRecordCreate.as_view(), name='create'),
    # path('view/', ..., name='view'),
    path('', BlogIndexView.as_view(), name='list'),
    # path('edit/<int:pk>/', ..., name='edit'),
    # path('delete/<int:pk>/', ..., name='edit'),


]