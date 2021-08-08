from django.http.response import HttpResponse
from django.shortcuts import render
from . models import  Products
from django.db.models import Q
from django.core.paginator import InvalidPage,EmptyPage




def index(request):
    return render(request,"index.html")


def shirts(request):
    shirts = Products.objects.filter(subcategory="Shirts")
    return render(request,'shirts.html',{"shirts":shirts}) 

def tshirts(request):
    tshirts = Products.objects.filter(subcategory="T-Shirts")
    return render(request,'tshirts.html',{"tshirts":tshirts})



def details(request,products_slug):
    try:
        details = Products.objects.filter(slug=products_slug)
    except Exception as e:
        raise e   
    return render(request,"details.html",{"details":details})




def serach(request):
    product=None
    Query = None
    if "q" in request.GET:
        Query=request.GET.get('q')
    product=Products.objects.all().filter(Q(name__icontains=Query)|Q(desc__icontains=Query))
    return render(request,"search.html",{"product":product,"query":Query})    