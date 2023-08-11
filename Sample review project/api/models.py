from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self) -> str:
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "product"

    def __str__(self) -> str:
        return self.title
