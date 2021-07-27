from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Products(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250) 
    def __str__(self):
        return self.name
    choices = (
        ('T-Shirts','T-Shirts'),
        ('Shirts','Shirts'),
        ('Jeans','Jeans'),
        ('Watches','Watches'),
        ('Saree','Saree'),
        ('Churidhar', 'Churidhar'),
        ('Skirts', 'Skirts'),
        ('Dresses','Dresses'),
    )
    subcategory = models.CharField(choices=choices, max_length=50,default = '1')
    img1 = models.ImageField(upload_to="pictures")
    img2 = models.ImageField(upload_to="pictures")
    img3 = models.ImageField(upload_to="pictures")
    desc = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)



