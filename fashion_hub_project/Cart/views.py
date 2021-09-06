import Cart
from django.shortcuts import render,redirect,get_object_or_404
from Cart.models import CartList, Items
from fashion_hub_app.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView, View
from .forms import CheckOutForm
from django.contrib import messages


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


class CheckOutView(View):
    def get(self,*args, **kwargs):
        form = CheckOutForm
        context ={
            'form':form
        }
        return render(self.request,"checkout.html",context)
    def post(self, *args, **kwargs):
        form = CheckOutForm(self.request.POST or None)
        print(self.request.POST)
        if form.is_valid():
            print("form is valid")
            return redirect("Cart:checkout")
        messages.warning(self.request,"Failed Checkout")
        return redirect("Cart:checkout")    





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
                