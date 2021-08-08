from django.urls import path
from fashion_hub_app import views


app_name='fashion_hub_app'

urlpatterns = [
   path('index',views.index, name="index"),
   path('shirts',views.shirts, name='shirts'),
   path('T-shirts',views.tshirts, name='tshirts'),
   path('Searchresult/',views.serach, name='search'),
   path('details/<slug:products_slug>',views.details, name='details')
 
   
    
    
    
]

