from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='restaurant'),
    path('order/', views.order, name='order'),
    path('order_confirm/<int:order_id>/', views.order_confirm, name='order_confirm'),
    path('about/', views.about, name='about'),
]