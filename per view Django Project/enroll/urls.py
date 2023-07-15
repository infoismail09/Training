from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [

    # path('',views.home,name='home_page'),
    path('',cache_page(60)(views.home),name='home_page'),
    path('home/',views.home),
    path('contact/',views.contact,name="contact_page"),

]