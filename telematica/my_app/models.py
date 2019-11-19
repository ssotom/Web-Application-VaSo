from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    picture = models.URLField()

class Customer(models.Model):
    id = models.IntegerField(primary_key = True, verbose_name='ID')
    name = models.CharField(max_length=32)
    adress = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    birth = models.DateField()
    email = models.EmailField()
    def __str__(self):
        return self.name

class Comment(models.Model):
    customer = models.ForeignKey(Customer, default=0, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, default=0, on_delete=models.PROTECT, related_name='comments')
    comment = models.TextField()
    def __str__(self):
        return self.comment
