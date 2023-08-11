from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from django_celery_project import settings
from django.utils import timezone
from datetime import timedelta

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    #timezone.localtime(users.date_time) + timedelta(days=2)
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "If you received mail, please Inform mr that i had sucess fully applied celery with django"
        # to_email = user.email
        to_email = ['ismailansar9988@gmail.com','ismailansari2292@gmail.com']
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list= to_email, # recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"