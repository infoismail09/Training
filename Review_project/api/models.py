from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Branch(models.Model):
    address = models.CharField(max_length=255)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='companybranch',null=True) 
