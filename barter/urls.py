
from django.contrib import admin
from django.urls import path,include
from products import views

urlpatterns = [
    path('',include('products.urls')),
    path('products/',include('products.urls')),
    
    path('admin/', admin.site.urls)
    
]
