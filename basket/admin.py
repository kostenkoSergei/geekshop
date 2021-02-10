from django.contrib import admin
from basket.models import Basket


class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'sum')
    search_fields = ('product__name',)


admin.site.register(Basket, BasketAdmin)
