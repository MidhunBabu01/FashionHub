from django.db import models
from django.template.defaultfilters import default
from django_countries.widgets import CountrySelectWidget
from fashion_hub_app.models import Products
from django.conf import settings
from django_countries.fields import CountryField

# Create your models here.
class CartList(models.Model):
    cart_id = models.CharField(max_length=50,unique=True)
    Date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id






class Items(models.Model):
    prodt = models.ForeignKey(Products,on_delete=models.CASCADE)
    cart = models.ForeignKey(CartList,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.prodt

    def total(self):
        return self.prodt.price*self.quantity



class Orderz(models.Model):
    cartt = models.ManyToManyField(Items)
    name = models.CharField(max_length=25,blank=False)
    email = models.EmailField(blank=True)
    mobile = models.CharField(blank=False,max_length=10 )
    address = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=15, blank=False)
    STATE_CHOICES = (
        ('Kerala','Kerala'),
        ('Tamilnaadu','Tamilnaadu'),
        ('Telangana','telangana')
    )
    ORDER_CHOICES = (
        ('order recieved','order recieved'),
        ('order processing','order processing'),
        ('on the way','on the way'),
        ('order cancelled','order cancelled')
    )
    state = models.CharField(max_length=25,choices=STATE_CHOICES, default='1')
    pin = models.IntegerField()
    country = CountryField()    
    # total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=25,choices=ORDER_CHOICES)
    def __str__(self):
        return str(self.name)
    
