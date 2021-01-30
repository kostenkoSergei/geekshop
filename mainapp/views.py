from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def index(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
        'title': 'каталог'
    }
    print(pk)  # для тестирования ссылок на продукты
    return render(request, 'mainapp/products.html', context)


def category(request, pk):
    context = {
        'products': Product.objects.filter(category=pk),
        'categories': ProductCategory.objects.all(),
        'title': ProductCategory.objects.get(pk=pk)
    }
    return render(request, 'mainapp/products.html', context)
