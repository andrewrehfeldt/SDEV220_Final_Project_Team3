from django.db import models
from django.conf import settings
from django.utils import timezone



# Create your models here.

class Customer(models.Model):
    customerName = models.CharField(max_length=100)
    customerEmail =  models.EmailField()
    
    def __str__(self):
        return self.customerName

class Menu(models.Model):
    dishName = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.dishName
    
class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    orderDate = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    items = models.ManyToManyField(Menu, through='OrderItem')
    
    def __str__(self):
        return f"{self.customer.customerName} - ${self.total_price}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, name='order_items')
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    customize = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return str(self.id)