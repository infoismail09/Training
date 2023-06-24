from django.shortcuts import render,redirect,HttpResponse
from .models import Task,Sub_Task
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .froms import CreateUserFrom
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# from django.views.decorators.cache import cache_page



def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def task_list(request):
    id=request.user.id
    # id=request.user.id with in below  object type owner =id then it show list of logged in user and secound way already user below (owner=request.user)
    get_task=Task.objects.filter(owner =id)
    context  = {'task':get_task}
    return render (request,'task_list.html',context)


def task_detail(request,id):
    if request.method=='GET':
        get_task=Task.objects.get(id=id)
        get_subtask=Sub_Task.objects.filter(task_id=id)
        subtask={'subtask':get_subtask,'task':get_task}
        return render(request,'task_detail.html',subtask)
    if request.method=="POST":
        get_task=Task.objects.get(id=id)
        subtask_name=request.POST.get('subtask_name')
        subtask=Sub_Task(subtask_name=subtask_name,task_id=id)
        subtask.save()
        return redirect('task_list')
    
    
def create_task(request):
    if request.method=="POST":
        task_name=request.POST.get('task_name')
        status=request.POST.get('status')
        if status=='complete':
            status=1
        else:
            status=0
        id=request.user.id
        owner_instance=User.objects.get(id=id)
        data=Task(task_name=task_name,status=status,owner=owner_instance)
        data.save()
        return redirect("task_list")

    return render(request,'create_task.html')


def update(request):
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
    return redirect("task_list")


def delete(request, id):
  member = Task.objects.get(id=id)
  member.delete()
  return redirect('task_list')


def registeruser(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    else:
        form=CreateUserFrom()
        if request.method=='POST':
         form=CreateUserFrom(request.POST)
         if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account Created Successfully for ' + user)
            return redirect('login')
    
        
    context={'form':form}
    return render(request,'register.html',context)


def loginuser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password')

         user=authenticate(request, username=username,password=password)

         if user is not None:
            login(request,user)
            return redirect('home')
         else:
            messages.info(request,'username and password is incorrect')

    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')















