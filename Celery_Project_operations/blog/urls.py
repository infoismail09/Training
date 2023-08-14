from django.urls import path
from . import views

urlpatterns = [
    path('resetpassword/',views.Reset_password_link,name='resetpassword'),
    
]