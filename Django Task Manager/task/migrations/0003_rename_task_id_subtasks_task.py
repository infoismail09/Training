# Generated by Django 4.2.2 on 2023-06-20 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_rename_owner_id_task_owner_alter_subtasks_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtasks',
            old_name='task_id',
            new_name='task',
        ),
    ]
