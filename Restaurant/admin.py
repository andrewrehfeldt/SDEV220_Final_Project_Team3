from django.contrib import admin
from .models import Menu, OrderItemDetails, CustomerOrder, OrderItem

# Register your models here.

admin.site.register(Menu)
admin.site.register(CustomerOrder)
admin.site.register(OrderItem)
admin.site.register(OrderItemDetails)