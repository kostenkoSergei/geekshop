from django.urls import path

from mainapp import views as mainapp_views

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp_views.index, name='index'),
    path('products/', mainapp_views.products, name='products'),
    path('product/<int:category_id>/', mainapp_views.products, name='product'),
    path('product/page/<int:page>/', mainapp_views.products, name='page'),
]
