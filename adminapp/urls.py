from django.urls import path

from adminapp import views as adminapp_views

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp_views.index, name='index'),
]
