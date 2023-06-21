from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_name', 'status','owner','created_at','updated_at')


class CreateUserForm(UserCreationForm):
   class Meta:

       class Meta:
        model = User
        fields = ['username','email','password1','password2','check']

