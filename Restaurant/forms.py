from django import forms
from .models import Menu, CustomerOrder, OrderItem, Customer

class CustomerOrderForm(forms.Form):
    item_ids = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = CustomerOrder
        fields = ['customerName', 'customerEmail', 'orderDate', 'item_ids']
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customerName', 'customerEmail']
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        
class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']
        