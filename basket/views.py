from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from mainapp.models import Product
from basket.models import Basket, BasketQuerySet
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse


@login_required
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

class BasketRemove(DeleteView):
    model = Basket
    def get_success_url(self):
        return reverse_lazy('auth:profile')


# @login_required
# def basket_remove(request, id):
#     basket = Basket.objects.get(pk=id)
#     basket.delete()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        basket = Basket.objects.get(pk=int(id))
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        context = {
            'baskets': baskets,
        }
        result = render_to_string('basket/basket.html', context)
        return JsonResponse({'result': result})
