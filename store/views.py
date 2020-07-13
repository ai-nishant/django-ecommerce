from django.shortcuts import render
from .models import Product , Order , Product , OrderItem
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
import json

class itemDetailView(DetailView):
    model = Product 
    template_name = 'single-product.html'

def index(request):
    return render(request,'index.html')


def store(request):
    product_list = Product.objects.all()
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
        'cartItems':cartItems
    }
    return render(request,'category.html' , context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer , complete= False)
        items = order.orderitem_set.all()
    else :
        items = []
        order = {'get_cart_total':0,
                'get_cart_items' :1
                }


    context = {
        'items':items,
        'order':order

    }
    return render(request,'cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer , complete= False)
        items = order.orderitem_set.all()
    else :
        items = []
        order = {'get_cart_total':0,
                'get_cart_items' :1
                }
    context = {
        'items':items,
        'order':order

    }
    return render(request,'checkout.html',context)


def singleProduct(request,id):
    return render(request,'single-product.html')


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)