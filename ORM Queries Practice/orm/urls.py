from django.urls import path
from . import views

urlpatterns = [
    path('album/',views.get_album,name="album"),
    path('song/',views.get_song,name="album")

]