from django.shortcuts import render
from django.contrib import messages
# Create your views here.
# from django.http import HttpResponse
from .models import Product
from datetime import date
from datetime import datetime, timedelta

# user details
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


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
    
def loginUser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            
        except:
            messages.error(request,'User does not exit,try to register')
            return redirect('register-student')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('products')
        else:
            messages.error(request,'username or password does not exist')
    context = {}
    return render(request, 'course/login.html',context)