from django.db import models
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







class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    mobile = models.IntegerField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    # sate = models.CharField
    pin = models.IntegerField()
    country =  CountryField()
    def __str__(self):
        self.user.username 

