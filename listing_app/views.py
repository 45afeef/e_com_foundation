from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import * 

# Create your views here.

def index(request):
    return HttpResponse("Hello from Listing App")

class ListingListView(ListView):
    model = Listing


class ProductListView(ListView):
    model = Product
    template_name = "listing_app/listing_list.html"


class ServiceListView(ListView):
    model = Service
    template_name = "listing_app/listing_list.html"


class ListingDetailView(DetailView):
    model = Listing


class ProductDetailView(DetailView):
    model = Product
    template_name = "listing_app/listing_detail.html"


class ServiceDetailView(DetailView):
    model = Service
    template_name = "listing_app/listing_detail.html"
