from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime


# Create your models here.

class Menu(models.Model):
    dishName = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.dishName
    
class CustomerOrder(models.Model):
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_email = models.EmailField(blank=True, null=True)
    orderDate = models.DateTimeField(default=datetime.datetime.now())
    total_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.customer_name} - Total Price: ${self.total_price}"
class OrderItem(models.Model):
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, blank=True, null=True)
    menu_items = models.ManyToManyField(Menu, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    
    def customer_name(self):
        return self.order.customer_name
    
    def __str__(self):
        return f"{self.customer_name()}'s Order has {self.quantity} items"

class OrderItemDetails(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, null=True)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField() 
    customization = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"{self.order_item.order} - {self.quantity} {self.menu_item}"