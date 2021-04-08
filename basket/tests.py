from django.test import TestCase
from django.test.client import Client
from basket.models import Basket
from authapp.models import User
from mainapp.models import Product, ProductCategory
from django.core.management import call_command


class TestBasketappSmoke(TestCase):

    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

        self.superuser = User.objects.create_superuser('django2', 'django2@geekshop.local', 'geekbrains')
        self.user = User.objects.create_user('tarantino', 'tarantino@geekshop.local', 'geekbrains')

        self.category = ProductCategory.objects.create(name='badaikin')
        self.product = Product.objects.create(name='badaikin', category=self.category, quantity=10)

    def test_basket_login_redirect(self):
        # без логина должен переадресовать
        # response = self.client.get('/auth/profile/')
        response = self.client.get('/auth/profile/')
        self.assertEqual(response.url, '/auth/login/?next=/auth/profile/')
        self.assertEqual(response.status_code, 302)

        # для залогиненого пользователя
        self.client.login(username='tarantino', password='geekbrains')
        response = self.client.get('/auth/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['baskets']), [])
        self.assertFalse(response.context['user'].is_anonymous)

    def test_basket_add(self):
        self.client.login(username='tarantino', password='geekbrains')
        response = self.client.get(f'/baskets/basket-add/{self.product.pk}/')
        self.assertTrue(Basket.objects.filter(product=self.product).exists())

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basket')
