from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_musician,name="musician-details"),
]