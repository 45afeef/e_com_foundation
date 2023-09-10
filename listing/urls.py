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
    path('listing/<slug:slug>',views.ListingDetailView.as_view(), name="listing-detail"),
    path('product/<slug:slug>',views.ProductDetailView.as_view(), name="product-detail"),
    path('service/<slug:slug>',views.ServiceDetailView.as_view(), name="service-detail"),
    path('cart/<int:id>/', cart, name="add-to-cart")
]
