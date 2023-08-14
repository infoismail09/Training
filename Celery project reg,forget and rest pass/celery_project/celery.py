from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

app = Celery('celery_project')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/kolkata')

app.config_from_object(settings, namespace='CELERY')

# celery beat

# app.conf.beat_schedule = {
#     'send-mail-every-day-at-4': {
#         'task': 'celeryapp.task.send_mail_to.',
#         'schedule': crontab(hour=16, minute=40),
#         # 'args':(2,)

#     }

# }

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
