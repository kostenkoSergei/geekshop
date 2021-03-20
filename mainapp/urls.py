from django.urls import path

from mainapp import views as mainapp_views
from django.views.generic import TemplateView

app_name = 'mainapp'

urlpatterns = [
    # path('', mainapp_views.index, name='index'),
    path('', TemplateView.as_view(template_name='mainapp/index.html'), name='index'),
    # path('products/', mainapp_views.products, name='products'),
    # path('product/<int:category_id>/', mainapp_views.products, name='product'),
    # path('product/page/<int:page>/', mainapp_views.products, name='page'),
    path('products/', mainapp_views.ProductView.as_view(), name='products'),
    path('product/<int:category_id>/', mainapp_views.ProductView.as_view(), name='product'),
    path('product/page/<int:page>/', mainapp_views.ProductView.as_view(), name='page'),
]
