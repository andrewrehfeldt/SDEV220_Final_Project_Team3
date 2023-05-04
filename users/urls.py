from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<int:user_id>/', login_required(views.user_profile), name='user_profile'),
    path('register/', views.user_register, name='register'),
]