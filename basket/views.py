from django.shortcuts import HttpResponseRedirect, get_object_or_404
from mainapp.models import Product
from basket.models import Basket


def basket_add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        basket = Basket(user=request.user, product=product)
    else:
        basket = baskets.first()
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, id):
    basket = Basket.objects.get(pk=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
