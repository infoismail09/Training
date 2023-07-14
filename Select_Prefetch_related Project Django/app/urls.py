from django.urls import path
from app import views

urlpatterns = [
    path('cust/', views.getcustomers, name='customers'),
    path('product/', views.getproducts, name='products'),
    path('order/', views.getorder, name='orders'),
    
]