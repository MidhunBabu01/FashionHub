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
    tshirts = Products.objects.filter(subcategory="M-T-Shirts")
    return render(request,'tshirts.html',{"tshirts":tshirts})

def jeans(request):
    jeans = Products.objects.filter(subcategory="Men-Jeans")
    return render(request,"jeans.html",{"jeans":jeans})

def watches(request):
    watches = Products.objects.filter(subcategory="Men-Watches")
    return render(request,"watches.html",{"watches":watches})

def top(request):
    top = Products.objects.filter(subcategory="Top")
    return render(request,"top.html",{"top":top})

def women_jeans(request):
    women_jeans = Products.objects.filter(subcategory="Women-Jeans")
    return render(request,"women_jeans.html",{"women_jeans":women_jeans})


def boys(request):
    boys = Products.objects.filter(subcategory="boys")
    return render(request,"boys.html",{"boys":boys})  


def girls(request):
    girls = Products.objects.filter(subcategory="girls")
    return render(request,"girls.html",{"girls":girls}) 



def saree(request):
    saree = Products.objects.filter(subcategory="Saree")
    return render(request,"saree.html",{'saree':saree})


def women_watch(request):
    w_watch = Products.objects.filter(subcategory="Women-Watches")
    return render(request,"womenwatch.html",{'w_watch':w_watch})









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