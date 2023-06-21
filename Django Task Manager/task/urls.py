from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('tasks/', views.task_list, name='task_list'),
    path('create_task/',views.create_task,name = 'create_task'),
    path('update_task/<str:pk>/',views.update_task,name='update_task'),
    path('delete_task/<str:pk>/',views.delete_task,name='delete_task'),
    path('register',views.Register,name='register')

]
