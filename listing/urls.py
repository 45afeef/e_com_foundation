from django.urls import path

from . import views

name = 'listing'
urlpatterns = [
    path('',views.index)
]
