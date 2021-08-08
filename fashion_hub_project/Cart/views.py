from django.shortcuts import render,redirect,get_object_or_404
from Cart.models import CartList, Items
from fashion_hub_app.models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def cart(request,total=0,count=0,cart_items=None):
    try:
        ct =CartList.objects.get(cart_id=c_id(request))
        ct_items = Items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            total +=(i.prodt.price*i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass   

    return render(request,"cart.html",{"ct_items":ct_items, "total":total, "count":count})



def c_id(request):
    carttt_id = request.session.session_key
    if not carttt_id:
        carttt_id = request.session.create()
    return carttt_id



def add_cart(request,product_id):
    product = Products.objects.get(id=product_id)
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
    except CartList.DoesNotExist:
        ct = CartList.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items = Items.objects.get(prodt=product,cart=ct)
        if c_items.quantity < c_items.prodt.stock:
            c_items.quantity+=1
        c_items.save()
    except Items.DoesNotExist:
        c_items =Items.objects.create(prodt=product,quantity=1,cart=ct)
        c_items.save()
    return redirect("Cart:addcart")         


def minus_button(request, product_id):
    ct = CartList.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Products,id=product_id)
    c_items = Items.objects.get(prodt=prod, cart=ct)
    if c_items.quantity>1:
        c_items.quantity-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect("Cart:addcart")
    

def delete_button(request,product_id):
    ct = CartList.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Products,id=product_id)
    c_items = Items.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect("Cart:addcart")
