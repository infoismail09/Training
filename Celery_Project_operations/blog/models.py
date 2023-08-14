from django.db import models


# Create your models here.


class Token(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
