from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from blog.models import BlogRecord


# Create your views here.

class BlogRecordCreate(CreateView):
    model = BlogRecord
    template_name = 'blog/blog_form.html'
    fields = ('title', 'body', 'preview', 'is_published')
    success_url = reverse_lazy('blog:list')


class BlogRecordIndexView(ListView):
    model = BlogRecord
    template_name = 'blog/blog_list.html'
    context_object_name = 'objects_list'


class BlogRecordDeatilView(DetailView):
    model = BlogRecord
    template_name = 'blog/blog_detail.html'
    context_object_name = 'objects_list'
