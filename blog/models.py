from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    details_text = models.CharField(max_length=2000)
    blog_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class BlogEntry(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    headline=models.CharField(max_length=200)
    body = models.TextField()
    publication_date = models.DateField(default=datetime.datetime.now)
    mod_date = models.DateField(default=datetime.today)
    

    def __str__(self):
        return self.headline





# to incorporate
# must be like everything app
# add payment app
# all of the application are pluralized