from django.urls import path
from fashion_hub_app import views


app_name='fashion_hub_app'

urlpatterns = [
   path('index',views.index, name="index"),
   path('shirts',views.shirts, name='shirts'),
   path('T-shirts',views.tshirts, name='tshirts'),
   path('Searchresult/',views.serach, name='search'),
   path('details/<slug:products_slug>',views.details, name='details'),
   path('jeans/',views.jeans, name='jeans'),
   path('watches/',views.watches, name="watches"),
   path('top',views.top,name="top"),
   path('women-jeans',views.women_jeans,name="women-jeans"),
   path('kids-section',views.boys,name="boys"),
   path('kids-sections',views.girls,name="girls"),
   path('womens-sections', views.saree, name="saree"),
   path('watches',views.women_watch, name="w_watch")  
   
    
]

