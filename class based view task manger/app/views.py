from django.shortcuts import render
from .models import Task,Sub_Task
from django.contrib.auth.models import User
from django.views import View

# Create your views here.

class task_list(View):
    def get(self,request):
        get_task = Task.objects.all()
        context = {'task':get_task}
        return render(request,'task_list.html',context)
    



