# Generated by Django 2.2.17 on 2021-04-07 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'позиция заказа', 'verbose_name_plural': 'позиции заказа'},
        ),
    ]