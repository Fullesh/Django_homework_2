from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product, Category


class indexListView(ListView):
    model = Product
    template_name = 'catalog/blog_list.html'
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


class ProductAddView(TemplateView):
    template_name = 'catalog/add_product.html'

    def get_context_data(self, **kwargs):
        context = {
            'objects_list': Category.objects.all()
        }
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_name = request.POST.get('product_name')
            product_description = request.POST.get('product_description')
            price_to_buy = request.POST.get('price_to_buy')
            product_image = request.POST.get('product_image')
            category = request.POST.get('category')
            info = {
                'name': product_name,
                'description': product_description,
                'image': product_image,
                'category': Category.objects.get(name=category),
                'price_to_buy': price_to_buy
            }
            Product.objects.get_or_create(**info)
        return render(request, self.template_name, self.get_context_data(**kwargs))
