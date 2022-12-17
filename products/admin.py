from django.contrib import admin

# Register your models here.
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description','price','stock','category','date_added','date_edited',)


admin.site.register(Product,ProductAdmin)

