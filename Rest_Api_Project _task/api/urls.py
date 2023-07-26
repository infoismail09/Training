from django.urls import path
from . import views

urlpatterns = [
    path('quotes/',views.quotes_list, name = 'quotes'),
    path('quotes/<int:pk>',views.quotes_details,name='quotes_details'),
]


