# from _typeshed import Self
# import Cart
from django import forms
from django.http.response import HttpResponse
from django.http import request
from django.shortcuts import render,redirect,get_object_or_404
from django.template.defaultfilters import add
from django.views.generic.base import TemplateView
from Cart.models import CartList, Items, Orderz
from fashion_hub_app.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView, View
from .forms import CheckOutForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def cart(request,total=0,count=0,cart_items=None):
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
        ct_items = Items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            total +=(i.prodt.price*i.quantity)
            count += i.quantity      
    except ObjectDoesNotExist:
        return redirect("Cart:cart2Details")
    return render(request,"cart.html",{"ct_items":ct_items, "total":total, "count":count})


def cart2(request):
    return render(request,"cart2.html") 






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



def count(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct = CartList.objects.filter(cart_id=c_id(request))
            cti = Items.objects.all().filter(cart=ct)
            for c in cti:
                item_count+=c.quantity
        except CartList.DoesNotExist:
            item_count = 0
        return render({"count":item_count})     


    
def checkout(request,total=0,count=0,cart_items=None):
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
        ct_items = Items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            total +=(i.prodt.price*i.quantity)
            count += i.quantity      
    except ObjectDoesNotExist:
        return redirect("Cart:cart2Details")
    form = CheckOutForm()
    if request.method=='POST':
        print(request.POST)
        form = CheckOutForm(request.POST)
        if form.is_valid():
            ct_items = Items.objects.filter(cart=ct,active=True)
            Orderz.objects.filter(cartt=ct_items)
            form.save()
            return redirect('Cart:order-successfull')
        else:
            return redirect('Cart:checkout')
    return render(request,"checkout.html",{'ct_items':ct_items,"total":total, "count":count, 'form':form})

    

def orderplaced(request):
    return render(request,"ordersuccess.html")
        
    
