from django.shortcuts import render


def index(request):
    return render(request, 'catalog/home.html')


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


def products(request):
    return render(request, 'catalog/products.html')