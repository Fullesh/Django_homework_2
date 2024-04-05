from django.contrib import admin
from django.urls import path, include
from blog.apps import BlogConfig
from blog.views import BlogRecordCreate, BlogRecordIndexView, BlogRecordDeatilView

app_name = BlogConfig.name


urlpatterns = [
    path('create/', BlogRecordCreate.as_view(), name='create'),
    path('view/<int:pk>', BlogRecordDeatilView.as_view(), name='view'),
    path('', BlogRecordIndexView.as_view(), name='list'),
    # path('edit/<int:pk>/', ..., name='edit'),
    # path('delete/<int:pk>/', ..., name='edit'),


]