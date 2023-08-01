from django.db import models

# Create your models here.

class Quotes(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name= 'product', null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

