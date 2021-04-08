from django.test import TestCase

from django.test.client import Client
from basket.models import Basket
from authapp.models import User
from mainapp.models import Product, ProductCategory
from ordersapp.models import Order, OrderItem
from django.core.management import call_command

class TestBasketappSmoke(TestCase):

    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

        self.superuser = User.objects.create_superuser('django2', 'django2@geekshop.local', 'geekbrains')
        self.user = User.objects.create_user('tarantino', 'tarantino@geekshop.local', 'geekbrains')

        self.category = ProductCategory.objects.create(name='badaikin')
        self.product_1 = Product.objects.create(name='badaikin', category=self.category, quantity=10, price=1000)
        self.product_2 = Product.objects.create(name='badaikin', category=self.category, quantity=10, price=2000)
        self.order = Order.objects.create(user=self.user)
        self.order_item_1 = OrderItem.objects.create(order=self.order, product=self.product_1, quantity=2)
        self.order_item_2 = OrderItem.objects.create(order=self.order, product=self.product_2, quantity=2)

    def test_order_quantity(self):
        self.assertEqual(self.order.get_total_quantity(), 4)

    def test_order_cost(self):
        self.assertEqual(self.order.get_total_cost(), 6000)

    def test_order_product_type_quantity(self):
        self.assertEqual(self.order.get_product_type_quantity(), 2)

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basket')