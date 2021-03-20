from django.shortcuts import render
from django.views.generic import ListView

from mainapp.models import Product, ProductCategory


class ProductView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'mainapp/products.html'
    paginate_by = 3

    def get_queryset(self):
        if self.request.GET.get('category_id'):
            return Product.objects.filter(category_id=self.kwargs['category_id'])
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context

# def products(request, category_id=None, page=1):
#     if category_id:
#         products = Product.objects.filter(category_id=category_id)
#     else:
#         products = Product.objects.all()
#     per_page = 3
#     paginator = Paginator(products.order_by('-price'), per_page)
#     products_paginator = paginator.page(page)
#     context = {
#         'categories': ProductCategory.objects.all(),
#         'products': products_paginator
#     }
#     return render(request, 'mainapp/products.html', context)
