from celery import shared_task
from django.core.mail import send_mail
from Demo_project import settings
import uuid


@shared_task(bind=True)
def send_reset_password_link(self):
    token = uuid.uuid4()
    reset_link = f"http://127.0.0.1:8000?token={token}"
    mail_subject = "Reset Password Mail"
    message = f'Click here to reset your password,{reset_link}'
    to_email = ['ismailansar9988@gmail.com','ismailansari2292@gmail.com']
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=to_email,
        fail_silently=False,
    )
    return "Mail Sent"