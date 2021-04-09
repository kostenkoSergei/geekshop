from django.urls import path

from adminapp import views as adminapp_views

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp_views.index, name='index'),
    path('admin-users-read/', adminapp_views.UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', adminapp_views.UserCreateView.as_view(), name='admin_users_create'),
    path('admin-users-update/<int:pk>/', adminapp_views.UserUpdateView.as_view(), name='admin_users_update'),
    path('admin-users-delete/<int:pk>/', adminapp_views.UserDeleteView.as_view(), name='admin_users_delete'),
    path('admin-products-read/', adminapp_views.ProductListView.as_view(), name='admin_products_read'),
    path('admin-products-create/', adminapp_views.ProductCreateView.as_view(), name='admin_products_create'),
    path('admin-products-update/<int:pk>/', adminapp_views.ProductUpdateView.as_view(), name='admin_products_update'),
    path('admin-products-delete/<int:pk>/', adminapp_views.ProductDeleteView.as_view(), name='admin_products_delete'),
    path('admin-categories-read/', adminapp_views.CategoryListView.as_view(), name='admin_categories_read'),
    path('admin-categories-create/', adminapp_views.CategoryCreateView.as_view(), name='admin_categories_create'),
    path('admin-categories-update/<int:pk>/', adminapp_views.CategoryUpdateView.as_view(),
         name='admin_categories_update'),
    path('admin-categories-delete/<int:pk>/', adminapp_views.CategoryDeleteView.as_view(),
         name='admin_categories_delete'),
]
