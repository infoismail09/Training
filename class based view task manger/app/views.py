from django.shortcuts import render,redirect
from .models import Task,Sub_Task
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.

class task_list(View):
    def get(self,request):
        get_task = Task.objects.all()
        context = {'task':get_task}
        return render(request,'task_list.html',context)

class task_detail(View):
    def get(self,request,id):
        if request.method=='GET':
            try:
                get_task=Task.objects.get(id=id)
            except Task.DoesNotExist:
                get_task=None
            if get_task:
                get_subtask=Sub_Task.objects.filter(task_id=id)
                sub_task={'subtask':get_subtask,'task':get_task}
                return render(request,'task_detail.html',sub_task)

    def post(self,request,id):        
        if request.method=="POST":
            get_task=Task.objects.get(id=id)
            subtask_name=request.POST.get('subtask_name')
            sub_task=Sub_Task(subtask_name=subtask_name,task_id=id)
            sub_task.save()
            return redirect('task_list')
    

class Create_task(View):
    def post(self,request,id):
        task_name = request.POST.get('task_name')
        status = request.POST.get('status')
        if status=='complete':
             status=1
        else:
            status=0
        owner_instance=User.objects.get(id=id)
        data=Task(task_name=task_name,status=status,owner=owner_instance)
        data.save()
        return redirect("task_list")
        
        return render (request,'create_task.html')

class Update_task(UpdateView):
    def post(self,request,id):
        id=request.POST.get('id')
        task_name=request.POST.get('task_name')
        status=request.POST.get('status')
        task_instance=Task.objects.get(id=id)
        task_instance.task_name=task_name
        if status=='complete':
            task_instance.status=1
        else:
            task_instance.status=0
        task_instance.save()
        return redirect("/")
    

class delete(View):
    def delete(request,pk):
        task=Task.objects.get(int=id)

        if request.method=='POST':
            task.delete()
            return redirect('task_list')





    



