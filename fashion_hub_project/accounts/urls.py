from django.urls import path
from accounts import views


app_name='accounts'

urlpatterns = [
    path('',views.index, name="index"),
    path('login',views.login, name="login"),
    path('index2',views.index2, name="index2"),

    
]
