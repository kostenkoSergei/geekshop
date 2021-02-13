from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from basket.models import Basket

from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView


# from django.db.models import Sum, F, FloatField


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('products:index'))
#     else:
#         form = UserLoginForm()
#     context = {'form': form}
#     return render(request, 'authapp/login.html', context)


class UserLoginView(LoginView):
    template_name = 'authapp/login.html'
    form_class = UserLoginForm


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрировались!!!')
#             return HttpResponseRedirect(reverse('auth:login'))
#     else:
#         form = UserRegisterForm()
#     context = {'form': form}
#     return render(request, 'authapp/register.html', context)


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('auth:login')
    form_class = UserRegisterForm
    success_message = 'Вы успешно зарегистрировались!!!'


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    # full_price = \
    #     Basket.objects.filter(user=request.user).aggregate(
    #         full_price=Sum(F('product__price') * F('quantity'), output_field=FloatField()))['full_price']
    # full_quantity = \
    #     Basket.objects.filter(user=request.user).aggregate(
    #         full_quantity=Sum('quantity'))['full_quantity']

    baskets = Basket.objects.filter(user=request.user)

    context = {
        'form': form,
        'baskets': baskets,
        # 'total_quantity': sum(basket.quantity for basket in baskets),
        # 'total_sum': sum(basket.sum() for basket in baskets)
        # 'full_price': full_price,
        # 'full_quantity': full_quantity,
    }
    return render(request, 'authapp/profile.html', context)
