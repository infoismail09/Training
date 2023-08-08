from django.db import models
from django.core.validators import FileExtensionValidator
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# Create your models here.

class Quotes(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    
class Categories(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Products(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE,related_name='product',null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
# # this signal create Auth Token for new user 
# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender,instance=None,created=False,**kwargs):
#     if created:
#         Token.objects.create(user=instance)

class Request_Log(models.Model):
    user_id = models.IntegerField(null=True)
    request_method = models.CharField(max_length=10)
    request_path = models.CharField(max_length=500)
    response_status = models.IntegerField()
    request_body=models.JSONField(null=True)
    remote_address = models.CharField(max_length=100)
    server_hostname = models.CharField(max_length=200)
    run_time = models.DecimalField(max_digits=23, decimal_places=20)
    timestamp = models.DateTimeField(auto_now=True)


class FAQs(models.Model):
    questions = models.CharField(max_length=255)
    answer = models.TextField(max_length=255)
    attachment = models.FileField(blank=True,validators=[FileExtensionValidator(allowed_extensions=["pdf"])]
)