from django.urls import path

from adminapp import views as adminapp_views

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp_views.index, name='index'),
    path('admin-users-read/', adminapp_views.admin_users_read, name='admin_users_read'),
    path('admin-users-create/', adminapp_views.admin_users_create, name='admin_users_create'),
    path('admin-users-update/<int:id>/', adminapp_views.admin_users_update, name='admin_users_update'),
    path('admin-users-delete/<int:id>/', adminapp_views.admin_users_delete, name='admin_users_delete'),
    path('admin-products-read/', adminapp_views.admin_products_read, name='admin_products_read'),
    path('admin-products-create/', adminapp_views.admin_products_create, name='admin_products_create'),
    path('admin-products-update/<int:id>/', adminapp_views.admin_products_update, name='admin_products_update'),
]
