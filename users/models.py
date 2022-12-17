from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    username = models.EmailField()
    password = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)

    # storing anonymous users
    # I will add more conponents
    # register with admin
    # add user sign up form
    # add user sign in form