from django.urls import path
from .import views


urlpatterns = [
    path('',views.set_cookie),
    path('get/',views.get_cookie),
    path('delete/',views.delete_Custom_cookie),
    path('session_set/',views.create_session),
    path('access/',views.access_session),
    path('delete_session/',views.delete_session),
]