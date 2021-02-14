from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# rewrote using view in mainapp/urls.py
# def index(request):
#     return render(request, 'mainapp/index.html')


# def products(request, category_id=None):
#     context = {'categories': ProductCategory.objects.all()}
#     if category_id:
#         products = Product.objects.filter(category_id=category_id)
#     else:
#         products = Product.objects.all()
#     context.update({'products': products})
#     return render(request, 'mainapp/products.html', context)

def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    per_page = 3
    paginator = Paginator(products.order_by('-price'), per_page)
    products_paginator = paginator.page(page)
    context = {
        'categories': ProductCategory.objects.all(),
        'products': products_paginator
    }
    return render(request, 'mainapp/products.html', context)
    # try:
    #     products_paginator = paginator.page(page)
    # except PageNotAnInteger:
    #     products_paginator = paginator.page(1)
    # except EmptyPage:
    #     products_paginator = paginator.page(paginator.num_pages)
