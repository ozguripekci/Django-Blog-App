from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    OPTIONS = {
        ('draft', 'Draft'),
        ('public', 'Published'),
    }
    title= models.CharField(max_length=50)
    content = models.TextField(max_length=100)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date= models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='draft')
    slug = models.SlugField(blank=True, unique=True)

