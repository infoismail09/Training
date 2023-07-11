# Generated by Django 4.2.2 on 2023-07-04 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Task', '0002_requestlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestlog',
            name='user',
            field=models.ForeignKey(blank=True, default='Anonymous User', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]