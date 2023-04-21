from django.contrib import admin
from .models import Menu, Customer, CustomerOrder, OrderItem

# Register your models here.

admin.site.register(Menu)
admin.site.register(Customer)
admin.site.register(CustomerOrder)
admin.site.register(OrderItem)