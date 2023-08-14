from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.mail import send_mail
from celery_project import settings
from celery import shared_task


@shared_task(bind=True)
def send_generate_password_link(self, email):
    reset_link = f'http://127.0.0.1:8000/api/generate-password/?email={email}'
    mail_subject = "generate password"
    message = f"Click here to generate your password\n\n{reset_link}"    
    to_email = email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )

# @shared_task(bind=True)
# def send_mail_after_register(self, email):
#     mail_subject = "Registraion Confirmation Mail"
#     message = "Congratulations you have succesfully registered"
#     to_email = email
#     send_mail(
#         subject=mail_subject,
#         message=message,
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[to_email],
#         fail_silently=True,
#     )


@shared_task(bind=True)
def send_reset_password_link(self, email):
    reset_link = f'http://127.0.0.1:8000/api/changepassword/?email={email}'
    mail_subject = "Reset Password Mail"
    message = f"Click here to reset your password\n\n{reset_link}"
    to_email = email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )


@shared_task(bind=True)
def send_change_password_email(self, email):
    mail_subject = "Reset Password Mail"
    message = "Password changed succesfully"
    to_email = email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )


# @shared_task(bind=True)
# def send_mail_to(self):
#     users = get_user_model().objects.all()
#     for user in users:
#         mail_subject = "Celery Testing"
#         message = "Testing Purpose"
#         to_email = user.email
#         send_mail(
#             subject=mail_subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[to_email],
#             fail_silently=True,
#         )
#     return "Done"
