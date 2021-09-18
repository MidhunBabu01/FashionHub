from django.urls import path
from Cart import views





app_name='Cart'

urlpatterns = [
      path('add_cart/',views.cart,name="addcart"),
      path('cartDetails/<int:product_id>/',views.add_cart,name="cartDetails"),
      path('min_product/<int:product_id>/',views.minus_button,name="minus"),
      path('del-product/<int:product_id>/',views.delete_button,name="del_product"),
      path('cartDetails/',views.cart2,name="cart2Details"),
      path('checkout/',views.checkout,name="checkout"),
      path('order-successfull/',views.orderplaced, name="order-successfull")
    
]

