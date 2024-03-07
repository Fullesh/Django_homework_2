from django.shortcuts import render

from catalog.models import Product, Category


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


def add_product(request):
    context = {
        'objects_list': Category.objects.all()
    }
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        price_to_buy = request.POST.get('price_to_buy')
        product_image = request.POST.get('product_image')
        category = request.POST.get('category')
        print(f'NEW PRODUCT WAS ADDED! INFO BELOW: \n'
              f'NAME: {product_name} \n'
              f'DESC: {product_description} \n'
              f'PRICE: {price_to_buy} \n'
              f'CATEGORY: {category} \n'
              f'IMG: {product_image}')
        info = {
            'name': product_name,
            'description': product_description,
            'image': product_image,
            'category': Category.objects.get(name=category),
            'price_to_buy': price_to_buy
        }
        Product.objects.get_or_create(**info)
    return render(request, 'catalog/add_product.html', context)
