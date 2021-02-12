from django.shortcuts import render, HttpResponseRedirect
from authapp.models import User
from mainapp.models import Product, ProductCategory
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')


# @user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('mainapp:index'))  # use reverse_lazy for success url
# def admin_users_read(request):
#     context = {'users': User.objects.all()}
#     return render(request, 'adminapp/admin-users-read.html', context)

class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('mainapp:index')))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users_read'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegisterForm()
#     context = {'form': form}
#     return render(request, 'adminapp/admin-users-create.html', context)


class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_update(request, id):
#     user = User.objects.get(pk=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users_read'))
#     else:
#         form = UserAdminProfileForm(instance=user)
#     context = {'form': form, 'current_user': user}
#     return render(request, 'adminapp/admin-users-update-delete.html', context)

class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users_read')
    context_object_name = 'current_user'

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'shop'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_delete(request, id):
#     user = User.objects.get(pk=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:admin_users_read'))

class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('mainapp:index'))  # use reverse_lazy for success url
def admin_products_read(request):
    context = {'products': Product.objects.all()}
    return render(request, 'adminapp/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products_read'))
        else:
            print(form.errors)
    else:
        form = ProductForm()
    context = {'form': form}
    print(context)
    return render(request, 'adminapp/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products_read'))
    else:
        form = ProductForm(instance=product)
    context = {'form': form, 'current_product': product}
    return render(request, 'adminapp/admin-products-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('admins:admin_products_read'))
