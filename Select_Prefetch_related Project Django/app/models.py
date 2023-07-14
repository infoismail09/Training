from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=256, null=True)
    email = models.EmailField(max_length=256,null=True)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True, blank=True)
    Product_name = models.CharField(max_length=30)
    product_type = models.CharField(max_length=30)
    product_price = models.IntegerField()

    def __str__(self) :
        return self.Product_name
    
class Order(models.Model):
    customer = models.ManyToManyField(Customer)
    ordered_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=True)
    transaction_id = models.CharField(max_length=256,null=True)

    def __str__(self):
        return self.transaction_id
