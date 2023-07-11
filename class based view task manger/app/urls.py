from django.urls import path
from . import views


urlpatterns = [
    path('',views.task_list.as_view(),name='task_list'),
    # path('Sub_task_lis/',views.Sub_task_list.as_view()),
    path('task/<int:id>',views.task_detail.as_view()),
    path('Create_task',views.Create_task.as_view(),name="Create_task"),
    path('Update_task',views.Update_task.as_view(),name="Update_task"),
    path('delete/<int:id>',views.delete.as_view(),name="delete"),
]


