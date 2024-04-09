from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.froms import ProductAddForm, VersionForm
from catalog.models import Product, Category, Version


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


class ProductUpdateView(UpdateView):
    model = Version
    template_name = 'catalog/product_form.html'
    form_class = VersionForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormSet(self.request.POST, self.object)
        else:
            context_data['formset'] = VersionFormSet(self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        
        return super().form_valid(form)
