from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import * 

# Create your views here.

def index(request):
    return HttpResponse("Hello from Listing App")

class ListingListView(ListView):
    model = Listing

class ListingDetailView(DetailView):
    model = Listing
