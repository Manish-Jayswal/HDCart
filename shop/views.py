from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides =  n// + ceil((n/4)-n//4)
    params = {'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')


def contact(request):
    return HttpResponse("We are in contact")


def tracker(request):
    return HttpResponse("We are in tracker")


def search(request):
    return HttpResponse("We are in search")

def prodView(request):
    return HttpResponse("We are in prodView")


def checkout(request):
    return HttpResponse("We are in checkout")