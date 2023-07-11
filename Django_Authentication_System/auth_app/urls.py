from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage,name='HomePage'),
    path('register/',views.Register,name='register-page'),
    path('login/',views.Login,name='lohin-page')

]