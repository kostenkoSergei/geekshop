# Generated by Django 2.2.17 on 2021-01-30 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(choices=[('MSK', 'Moscow'), ('NY', 'New York'), ('LA', 'Los Angeles'), ('TKO', 'Tokyo')], default='MSK', max_length=24),
        ),
    ]
