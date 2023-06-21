from django.contrib import admin
from .models import Task,subtasks

# Register your models here.
admin.site.register(Task)
admin.site.register(subtasks)
