from django.urls import path
from mainapp import views

urlpatterns = [
    # path('sendmail/', views.send_mail_to_all, name='sendmail'),
    # path('register/', views.signup_mail, name='register'),
    path('registerapi/', views.register_user, name='register'),
    path('resetpassword/', views.reset_password_link, name='resetpassword'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('generate-password/', views.generate_password, name='generate-password')


]
