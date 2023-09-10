from django.urls import path

from . import views

name = 'listing'
urlpatterns = [
    path('',views.index),
    path('a',views.ListingListView.as_view(), name="listing-list"),
    path('a/<int:pk>',views.ListingDetailView.as_view(), name="listing-detail")
]
