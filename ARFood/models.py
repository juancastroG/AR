# ARFood/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

class Food(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gltf = models.FileField(upload_to='models/', null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='productos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
