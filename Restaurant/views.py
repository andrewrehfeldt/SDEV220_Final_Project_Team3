from django.shortcuts import render, redirect
from django.views import View
from .models import Menu, Customer, CustomerOrder, OrderItem
from .forms import OrderForm

# Create your views here.

def menu_list(request):
    menu_items = Menu.objects.all()
    return render(request, 'Restaurant/menu.html', {'menu_items': menu_items})


def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            customerName = form.cleaned_data['customerName']
            customerEmail = form.cleaned_data['customerEmail']
            item_ids = form.cleaned_data['item_ids']
            orderItems = form.cleaned_data['orderItems']
            
            order = CustomerOrder.objects.create(customerName=customerName, customerEmail=customerEmail)
            
            for i in item_ids:
                menu_item = Menu.objects.get(id=item_ids[i])
                quantity = orderItems[i]
                order_item = OrderItem.objects.create(menu_item=menu_item, quantity=quantity)
                order.items.add(order_item)
            
            order.total_price = order.get_total_price()
            order.save()
            
            return redirect(request, 'Restaurant/order_confirm', order_id=order.id)
    else:
        form = OrderForm()
    menu_items = Menu.objects.all()
    context = {'menu_items': menu_items, 'form': form}
    return render(request, 'Restaurant/order.html', context)

def order_confirm(request, order_id):
    order = CustomerOrder.objects.get(id=order_id)
    return render(request, 'Restaurant/order_confirm.html', {'order': order})

def about(request):
    return render(request, 'Restaurant/about.html', {})