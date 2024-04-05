from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from blog.models import BlogRecord


# Create your views here.

class BlogRecordCreate(CreateView):
    model = BlogRecord
    template_name = 'blog/blog_form.html'
    fields = ('title', 'body', 'preview', 'is_published')
    success_url = reverse_lazy('blog:list')


class BlogIndexView(ListView):
    model = BlogRecord
    template_name = 'blog/blog_list.html'
