from django.urls import path
from . import views

urlpatterns = [
    path('',views.StudentList.as_view(),name="List-Student-api"),
    path('create',views.StudentCreate.as_view(),name="create-Student-api"),
    path('retrieve/<int:pk>/',views.StudentRetrieve.as_view(),name="retrieve-Student-api"),
    path('update/<int:pk>/',views.Studentupdate.as_view(),name="update-Student-api"),
    path('delete/<int:pk>/',views.Studentdelete.as_view(),name="delete-Student-api"),
]