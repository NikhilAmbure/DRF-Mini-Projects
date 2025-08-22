from django.db import models

# Create your models here.

class Product(models.Model): 
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

