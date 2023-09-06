from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True) # isse hum age user delete kare to uske post me null dekhyega kisne create kia hai and post delete nahi hoga
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=80)
    post_publish_date = models.DateField()


