from django.urls import path

from . import views

from django.http import HttpResponse
def cart(request, id):
    return HttpResponse(f"This is the cart of {id}")

name = 'listing'
urlpatterns = [
    path('',views.index),
    path('listings',views.ListingListView.as_view(), name="listing-list"),
    path('products',views.ProductListView.as_view(), name="product-list"),
    path('services',views.ServiceListView.as_view(), name="service-list"),
    path('listing/<int:pk>',views.ListingDetailView.as_view(), name="listing-detail"),
    path('product/<int:pk>',views.ProductDetailView.as_view(), name="product-detail"),
    path('service/<int:pk>',views.ServiceDetailView.as_view(), name="service-detail"),
    path('cart/<int:id>/', cart, name="add-to-cart")
]
