from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductAddForm, VersionForm
from catalog.models import Product, Version


class indexListView(ListView, LoginRequiredMixin):
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


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'objects_list'


class ProductAddView(CreateView, LoginRequiredMixin):
    model = Product
    template_name = 'catalog/add_product.html'
    form_class = ProductAddForm
    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductAddForm
    success_url = reverse_lazy('catalog:index')
    perms = ('catalog.edit_publication', 'catalog.edit_description', 'catalog.edit_categories')

    def get_form_class(self):
        if self.request.user.is_staff and self.request.user.has_perms(perm_list=self.perms) \
                and not self.request.user.is_superuser:
            return ProductAddForm
        else:
            if self.request.user != self.get_object().owner:
                raise PermissionDenied
            else:
                return ProductAddForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        Versionformset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = Versionformset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = Versionformset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.owner = self.request.user
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        
        return super().form_valid(form)


class ProudctDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:index')
    permission_required = 'catalog.delete_product'


