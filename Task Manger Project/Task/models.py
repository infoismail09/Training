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

# Another way to reflect changes on admin panel with formated string
    # def __str__(self):
    #     return f"{self.task_name} {self.created_at} {self.updated_at}"

    
# Created subtask model

class Sub_Task(models.Model):
    subtask_name = models.CharField(max_length=255)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subtask_name
    
# Another way to reflect changes on admin panel with formated string

    # def __str__(self):
    #     return f"{self.task} {self.subtask_name} {self.created_at}"


# created simple middleware which will log the following data model named RequestLog

class RequestLog(models.Model):
    user = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,null=True)
    date_time = models.DateTimeField(auto_now=True)





