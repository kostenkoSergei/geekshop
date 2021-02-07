from django.db import models
from django.contrib.auth.models import AbstractUser

CITIES_CHOICES = (
    ('MSK', 'Moscow'),
    ('NY', 'New York'),
    ('LA', 'Los Angeles'),
    ('TKO', 'Tokyo'),
)


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.SmallIntegerField(blank=True, null=True)
    city = models.CharField(max_length=24,
                            choices=CITIES_CHOICES,
                            default="MSK",
                            blank=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
