from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    stock = models.IntegerField()
    url = models.URLField(max_length=5083)
    category = models.CharField(max_length=200)