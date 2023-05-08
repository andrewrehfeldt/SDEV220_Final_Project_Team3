from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('menu_list/', views.menu_list, name='menu_list'),
    path('order/', views.order, name='order'),
    path('order_confirm/<int:pk>/', views.order_confirm, name='order_confirm'),
    path('about/', views.about, name='about'),
]