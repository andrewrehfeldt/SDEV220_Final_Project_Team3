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
    dishPrice = models.DecimalField(max_digits=5, decimal_places=2)
    finishTime = models.IntegerField()
    
    def __str__(self):
        return self.dishName
    
class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Menu, blank=True)
    #customize = models.TextField(blank=True, null=True, max_length=200)
    orderDate = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    
    def get_total_price(self):
        total_price = 0
        for item in self.items.all():
            total_price += item.get_item_price()
        return total_price
    
    def __str__(self):
        return f"{self.customer}'s order on {self.orderDate}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def get_item_price(self):
        return (self.menu_item.dishPrice * self.quantity)
        
    def __str__(self):
        return f"{self.menu_item.dishName} x {self.quantity} in order {self.order.id}"
    
    