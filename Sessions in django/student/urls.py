from django.urls import path
from .import views

urlpatterns = [
    path('set/',views.setsession,name='set-session'),
    path('get/',views.getsession,name='get-session'),
    path('del/',views.delsession,name='del-session'),
    path('set1/',views.settestcookies,name='set-Cookies'),
    path('get2/',views.checktestcookies,name='get-Cookies'),
    path('del3/',views.deltestcookies,name='del-Cookies'),
]