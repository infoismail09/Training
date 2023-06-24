from django.contrib import admin
from .models import Task,Sub_Task

# Register your models here.

admin.site.register(Task)
admin.site.register(Sub_Task)

# Another way to register Model on admin panel
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ['owner_id','task_name','created_at','updated_at']
# admin.site.register(Task, TaskAdmin)

# class TaskAdmin(admin.ModelAdmin):
#     list_display = ['subtask_name','created_at']
# admin.site.register(Sub_Task, TaskAdmin)

