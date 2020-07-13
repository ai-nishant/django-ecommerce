from django.urls import path
from .views import (    
    store , 
    cart , 
    checkout,
    singleProduct,
    itemDetailView,
    updateItem )


app_name = 'store'

urlpatterns = [
    path('detail/<pk>/',itemDetailView.as_view(),name='itemDetailView'),
    path('product/<id>/',checkout,name='checkout'),
    path('store',store,name='store'),
    path('cart',cart,name='cart'),
    path('checkout',checkout,name='checkout'),
    path('updateItem/', updateItem,name='updateItem')
]
