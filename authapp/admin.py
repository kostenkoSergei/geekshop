from django.contrib import admin

from authapp.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'avatar', 'username', 'email', 'age', 'city')


admin.site.register(User, UserAdmin)
