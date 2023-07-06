from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Status(models.IntegerChoices):
    Complete = 1
    InComplete = 0
    
# Created Task model

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    status= models.IntegerField(choices=Status.choices)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name

    
class Sub_Task(models.Model):
    subtask_name = models.CharField(max_length=255)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subtask_name

