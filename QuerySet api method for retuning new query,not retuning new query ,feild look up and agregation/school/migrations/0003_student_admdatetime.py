# Generated by Django 4.2.3 on 2023-07-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='admdatetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
