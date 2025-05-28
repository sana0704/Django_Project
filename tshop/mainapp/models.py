from django.db import models

# Create your models here.

#django.db contains all the necessary tools and function for db connectivity

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    stock = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', null=True) 
    desc = models.TextField(max_length=500, null = True)


# overriding the __str__ method 
    def __str__(self):
        return f"Product > {self.name}"
    
