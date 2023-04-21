from django import forms
from .models import Menu

class OrderForm(forms.Form):
    model = Menu
    customerName = forms.CharField(max_length=50)
    customerEmail = forms.EmailField()
    orderItems = forms.ModelMultipleChoiceField(
        queryset=Menu.objects.all(),
        #choices=[(item.id, item.dishName) for item in Menu.objects.all()], 
        widget=forms.CheckboxSelectMultiple()
        )