from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Basket(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title