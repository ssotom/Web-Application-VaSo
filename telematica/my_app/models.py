from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    picture = models.URLField()

class Customer(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=32)
    adress = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    birth = models.DateField()
    email = models.EmailField()

class Comment(models.Model):
    user = models.ForeignKey(Customer, related_name='user_id', on_delete=models.CASCADE)
    product_id = models.IntegerField(unique=True, default=0)
    comment = models.TextField()
