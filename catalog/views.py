from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from catalog.froms import ProductAddForm
from catalog.models import Product, Category


class indexListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'objects_list'


class contactsPageView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f"You have new feedback! Info: \n"
                  f"Subject_name: {name} \n"
                  f"Subject_phone: {phone} \n"
                  f"Subject_message: {message}")
        return render(request, self.template_name)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'objects_list'


class ProductAddView(CreateView):
    model = Product
    template_name = 'catalog/add_product.html'
    form_class = ProductAddForm
    success_url = reverse_lazy('catalog:index')