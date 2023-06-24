from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('task_list/',views.task_list,name='task_list'),
    path('task/<int:id>',views.task_detail,name='task_detail'),
    path('create_task',views.create_task,name='create_task'),
    path('update',views.update, name='update'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('register/', views.registeruser,name='register'),
    path('login/', views.loginuser,name='login'),
    path('logout/', views.logoutuser,name='logout'),


]