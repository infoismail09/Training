from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm,CreateUserForm
from django.http import HttpResponse
from django.contrib import messages

def home(request):
    return render(request,'task/index.html')

# to view all task below function is used

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks})

# this function is to create new task

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task/create_task.html', {'form': form})


# below function is for updating task

def update_task(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    context = {'form': form}
    return render(request,'task/update_task.html',context=context )


# now creating function for deleting task:-

def delete_task(request,pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request,'task/delete_task.html')
        

def Register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User registered Sucessfuully!')
        
    context = {'form':form}

    return render(request,'register.html',context=context)
        

        