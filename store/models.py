from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render , reverse

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    email =models.CharField(max_length=40)

    def __str__(self):
        return self.name
    

class ProductCategory(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=10)
    description = models.CharField(max_length=100)
    availability= models.BooleanField(default=True)
    category = models.ManyToManyField(ProductCategory)
    image = models.ImageField(null=True,blank=True)
    digital = models.BooleanField(default=False,null=True,blank=True)


    def __str__(self):
        return self.name


    @property
    def ImageUrl(self):
        try :
            url = self.image.url

        except:
            url = ''
        return url
    
    def get_absolute_url(self):
        return reverse('store:itemDetailView', kwargs={"pk": self.pk})
    

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank = True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.IntegerField()
    

    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
            return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0,null = True)
    date_added  = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return str(self.product.name)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total



class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)    
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address =models.CharField(max_length=150,null=True)
    city=models.CharField(max_length=150,null=True)
    state=models.CharField(max_length=150,null=True)
    pincode=models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200,null=True)

    date_added = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.address
    




