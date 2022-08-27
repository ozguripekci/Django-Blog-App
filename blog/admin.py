from django.contrib import admin
from .models import Category, Post, Like, Comment, PostView
# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(PostView)

