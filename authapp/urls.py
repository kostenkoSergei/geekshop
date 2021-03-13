from django.urls import path

from authapp import views as authapp_views

app_name = 'authapp'

urlpatterns = [
    # path('login/', authapp_views.login, name='login'),
    path('login/', authapp_views.UserLoginView.as_view(), name='login'),
    # path('register/', authapp_views.register, name='register'),
    path('register/', authapp_views.UserRegisterView.as_view(), name='register'),
    path('logout/', authapp_views.logout, name='logout'),
    path('profile/', authapp_views.profile, name='profile'),
    path('verify/<int:user_id>/<hash>', authapp_views.verify, name='verify'),
]
