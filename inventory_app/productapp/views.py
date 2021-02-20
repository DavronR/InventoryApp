from django.shortcuts import render
from django.http import HttpResponse
from django import template
from .models import Product

def index(request):
    products = Product.objects.all() 
    return render(request, 'productapp/products.html', {"products": products})

# Create your views here.
