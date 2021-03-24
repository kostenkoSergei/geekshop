from basket.models import Basket


def user_basket(request):
    user_basket = None

    if request.user.is_authenticated:
        user_basket = Basket.objects.filter(user=request.user)
        user_basket_counter = Basket.objects.filter(user=request.user).count()

    return {
        'user_basket': user_basket,
        'user_basket_counter': user_basket_counter,
    }
