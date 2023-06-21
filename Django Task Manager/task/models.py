from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Status(models.IntegerChoices):
   Complete = 1
   InComplete = 0


class Task (models.Model):
    task_name = models.CharField(max_length=255)
    status = models.IntegerField(choices=Status.choices)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task_name
    

class subtasks(models.Model):
    subtasks_name = models.CharField(max_length=255)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subtasks_name





