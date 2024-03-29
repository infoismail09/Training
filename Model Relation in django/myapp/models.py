from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    # user = models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True) # in this user will not delete if it will protect
    # user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,limit_choices_to={'is_staff':True}) # in this only staff user can create page
    page_name = models.CharField(max_length=100)
    page_cat = models.CharField(max_length=100)
    page_publish_date = models.DateField()

class Like(Page):
    Panna = models.OneToOneField(Page,on_delete=models.CASCADE,primary_key=True,parent_link=True)
    likes = models.IntegerField()