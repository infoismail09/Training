from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="Home"),
    # path('excp',views.excp,name="excp"),
    path('user_info',views.user_info,name = 'user_info'),
]