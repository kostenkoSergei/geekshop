from django.db import models

from authapp.models import User
from mainapp.models import Product
from django.utils.functional import cached_property


class BasketQuerySet(models.QuerySet):
    def delete(self):
        """for deleting group of objects"""
        for object in self:
            object.refresh_quantity()
        super().delete()


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    @cached_property
    def get_items_cached(self):
        return self.user.basket.select_related()

    def total_quantity(self):
        # baskets = Basket.objects.filter(user=self.user)
        baskets = self.get_items_cached
        return sum(basket.quantity for basket in baskets)

    def total_sum(self):
        # baskets = Basket.objects.filter(user=self.user)
        baskets = self.get_items_cached
        return sum(basket.sum() for basket in baskets)

    def delete(self, using=None, keep_parents=False):
        self.product.quantity += self.quantity
        self.product.save()
        super().delete()

    def refresh_quantity(self):
        if self.pk:
            self.product.quantity -= self.quantity - Basket.objects.get(pk=self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()

    def save(self, *args):
        self.refresh_quantity()
        super().save(*args)

    class Meta:
        verbose_name = 'Корзина товаров'
        verbose_name_plural = 'Корзины товаров'
