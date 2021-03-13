from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

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
    activation_key = models.CharField(max_length=64, blank=True, null=True)
    activation_key_expires = models.DateTimeField(default=now() + timedelta(hours=48))

    def is_activation_key_expired(self):
        return False if now() <= self.activation_key_expires else True


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
