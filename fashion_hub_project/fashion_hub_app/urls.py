from django.urls import path
from fashion_hub_app import views
from accounts import views

app_name='fashion_hub_app'

urlpatterns = [
    path('',views.index, name="index")
    
]

