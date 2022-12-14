from django.db import models

# Create your models here.
CATEGORY = (
    ("FOOD","Food"),
    ("Electronics","Electronics"),
)


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    stock = models.IntegerField()
    url = models.URLField(max_length=5083)
    category=models.CharField(max_length=200,default=None,choices=CATEGORY)
    date_added = models.DateField(auto_now_add=True,null=True)
    date_edited = models.DateField(auto_now=True,null=True)
    