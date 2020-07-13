from django.shortcuts import render
from .models import homepageinfo
from store.models import Product , Order , OrderItem

def index(request):
    product_list = Product.objects.all()
    data = homepageinfo.objects.latest('date_updated')
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer , complete= False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else :
        items = []
        order = {'get_cart_total':0,
                'get_cart_items' :1
                }
        cartItems = order['get_cart_items']

    context = {
        'products' : product_list,
        'cartItems':cartItems,
        'data' : data
    }
    
   
    return render(request,'index.html',context)