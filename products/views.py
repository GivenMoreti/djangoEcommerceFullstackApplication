from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})

def about(request):
    return HttpResponse("About")