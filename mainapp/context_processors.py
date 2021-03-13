from basket.models import Basket


def user_basket(request):
    user_basket = None

    if request.user.is_authenticated:
        user_basket = Basket.objects.filter(user=request.user)

    return {
        'user_basket': user_basket,
    }
