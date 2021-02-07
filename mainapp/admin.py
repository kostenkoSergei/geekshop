from django.contrib import admin
from mainapp.models import ProductCategory, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_description', 'price')


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
