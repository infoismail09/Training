from django.urls import path
from . import views


urlpatterns = [
    path('',views.task_list.as_view(),name='task_list'),

]