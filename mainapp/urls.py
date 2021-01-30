from django.urls import path

from mainapp import views as mainapp_views

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp_views.index, name='index'),
    path('products/', mainapp_views.products, name='products'),
    path('products/<int:pk>/', mainapp_views.category, name='category'),  # отображает определенную категорию
    path('product/<int:pk>/', mainapp_views.products, name='product'),  # отображает конкретный продукт
]
