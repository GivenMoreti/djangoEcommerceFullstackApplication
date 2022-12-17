from django.shortcuts import render
# Create your views here.
# from django.http import HttpResponse
from .models import Product
from datetime import date
from datetime import datetime, timedelta


def index(request):
    products = Product.objects.all().order_by('name')
    return render(request,'index.html',{'products':products})

def about(request):
    return render(request,"About.html")

def discount(request):
    # date_of_stock = datetime.now()-timedelta(days=7)
    # date_of_stock= datetime.date(2022,11,26)
    # discount_products = Product.objects.all().filter(date_of_stock)
    discount_products = Product.objects.filter(category='Fruits')
    return render(request,'discount.html',{'discount_products':discount_products}) 
    