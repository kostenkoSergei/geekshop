from django.db import transaction
from django.shortcuts import render, HttpResponseRedirect, Http404, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm, ShopUserProfileEditForm
from basket.models import Basket

from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from .models import User
from .utils import send_virify_email


def verify(request, user_id, hash):
    user = User.objects.get(pk=user_id)
    if user.activation_key == hash and not user.is_activation_key_expired():
        user.is_active = True
        user.activation_key = None
        user.save()
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'authapp/verification.html')
        # return render(request, 'authapp/404_page.html')
    raise Http404

def handle_page_not_found(request, exception, template_name="authapp/404_page.html"):
    return render(request,template_name)


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
    success_message = 'Проверьте почту!!!'

    def post(self, request, *args, **kwargs):
        """rewrote post method to add send mail verification logic"""
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_virify_email(user)
            messages.success(request, 'Проверьте почту!!!')
            return HttpResponseRedirect(reverse_lazy('auth:login'))
        return render(request, 'authapp/register.html', {'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))


@login_required
@transaction.atomic
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(data=request.POST, instance=request.user.shopuserprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            # profile_form.save()

            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)
    # full_price = \
    #     Basket.objects.filter(user=request.user).aggregate(
    #         full_price=Sum(F('product__price') * F('quantity'), output_field=FloatField()))['full_price']
    # full_quantity = \
    #     Basket.objects.filter(user=request.user).aggregate(
    #         full_quantity=Sum('quantity'))['full_quantity']

    baskets = Basket.objects.filter(user=request.user)

    context = {
        'form': form,
        'profile_form': profile_form,
        'baskets': baskets,
        # 'total_quantity': sum(basket.quantity for basket in baskets),
        # 'total_sum': sum(basket.sum() for basket in baskets)
        # 'full_price': full_price,
        # 'full_quantity': full_quantity,
    }
    return render(request, 'authapp/profile.html', context)
