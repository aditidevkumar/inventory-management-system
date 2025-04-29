from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Mobile', 'Mobile'),
        ('Laptop', 'Laptop'),
        ('Smartwatch', 'Smartwatch'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    description = models.TextField(max_length=75)
    image = models.ImageField(upload_to='products/', default='default.jpg')

    def __str__(self):
        return self.name