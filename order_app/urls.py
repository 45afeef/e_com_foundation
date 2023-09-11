from django.urls import path

from . import views

name = 'order_app'
urlpatterns = [
    path('cart',views.cart)
]
