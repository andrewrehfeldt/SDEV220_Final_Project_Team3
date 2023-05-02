from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail
from .models import Menu, CustomerOrder, OrderItem, OrderItemDetails


# Create your views here.

def menu_list(request):
    menu_items = Menu.objects.all()
    return render(request, 'Restaurant/menu.html', {'menu_items':menu_items})


def order(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        order_items = {
            'items': []
        }
        
        items = request.POST.getlist('items[]')
        
        for item in items:
            menu_item = Menu.objects.get(pk=int(item))
            quantity = int(request.POST.get(f'quantity_{item}'))
            customization = request.POST.get(f'customization_{item}')
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.dishName,
                'price': menu_item.price,
                'quantity': quantity,
                'customization': customization
            }
            order_items['items'].append(item_data)
            
        total_price = 0
        quantity = 0
        item_ids = []
        
        for item in order_items['items']:
            total_price += item['price'] * item['quantity']
            item_ids.append(item['id'])
            quantity += item['quantity']
        
        customer_order = CustomerOrder.objects.create(
            customer_name=name,
            customer_email=email,
            total_price=total_price
        )
        print(customer_order)
        
        order_item = OrderItem.objects.create(
            order=customer_order,
            quantity=quantity
        )
        order_item.menu_items.set(item_ids)
        print(order_item)
        for item in order_items['items']:
            menu_item = Menu.objects.get(pk=item['id'])
            order_item_details =  OrderItemDetails.objects.create(
                order_item=order_item,
                menu_item=menu_item,
                quantity=item['quantity'],
                customization=item['customization']
            )
        print(order_items)
        return redirect('order_confirm', pk=order_item.pk)
        
    else:
        pass
    menu_items = Menu.objects.all()
    return render(request, 'Restaurant/order.html', {'menu_items':menu_items})
    
def order_confirm(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    order_item_details = OrderItemDetails.objects.filter(order_item=order_item)
    context = {
        'order_item': order_item,
        'order_item_details': order_item_details
    }
    
    return render(request, 'Restaurant/order_confirm.html', context=context)

def about(request):
    return render(request, 'Restaurant/about.html', {})