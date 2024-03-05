from django.shortcuts import render

from catalog.models import Product


def index(request):
    context = {
        'objects_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"You have new feedback! Info: \n"
              f"Subject_name: {name} \n"
              f"Subject_phone: {phone} \n"
              f"Subject_message: {message}")
    return render(request, 'catalog/contacts.html')


def one_product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
    }
    return render(request, 'catalog/product.html', context)
