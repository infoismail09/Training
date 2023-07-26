from django.urls import path
from . import views

urlpatterns = [
    path('func/',views.myview,name='func'),
    path('cl',views.Myview.as_view(),name='cl'),
    path('subcl',views.MyViewChild.as_view(),name='subcl'),

]