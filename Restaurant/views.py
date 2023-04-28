from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Menu, Customer, CustomerOrder, OrderItem
from .forms import OrderItemForm, CustomerOrderForm, CustomerForm

# Create your views here.

def menu_list(request):
    menu_items = Menu.objects.all()
    return render(request, 'Restaurant/menu.html', {'menu_items':menu_items})


def order(request):S
    if request.method == 'POST':
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            customer = form.cleaned_data.get('customer')
            item_ids = request.POST.getlist('item_ids')
            order_items = []
            total_price = 0
        
            for item_id in item_ids:
                menuItem = Menu.objects.get(pk=item_id)
                quantity= int(request.POST.get(f'quantity_{item_id}', 0))
                if quantity > 0:
                    order_item = OrderItem(menu_item=menuItem, price=menuItem.price, quantity=quantity)
                    order_item.save()
                    order_items.append(order_item)
                    total_price += (menuItem.price * quantity)
            
            customer_order = CustomerOrder(customer=customer, total_price=total_price)
            customer_order.save()
            customer_order.items.set([o.id for o in order_items])S
            
            messages.success(request, 'Order placed successfully!')
            return redirect('order_confirm', pk=customer_order.pk)
    else:
        form = CustomerForm()
    menu_items = Menu.objects.all()
    return render(request, 'Restaurant/order.html', {'menu_items': menu_items, 'form': form})

def order_confirm(request, pk):
    customer_order = get_object_or_404(CustomerOrder, pk=pk)
    order_items = customer_order.items.all()
    context = {'customer_order': customer_order, 'order_items': order_items}
    return render(request, 'Restaurant/order_confirm.html', context)

def about(request):
    return render(request, 'Restaurant/about.html', {})