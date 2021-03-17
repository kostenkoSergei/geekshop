from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver

CITIES_CHOICES = (
    ('MSK', 'Moscow'),
    ('NY', 'New York'),
    ('LA', 'Los Angeles'),
    ('TKO', 'Tokyo'),
)


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.SmallIntegerField(blank=True, null=True, default=18)
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


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(User, unique=True, null=False,
                                db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='теги', max_length=128,
                               blank=True)
    aboutMe = models.TextField(verbose_name='о себе', max_length=512,
                               blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1,
                              choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()
