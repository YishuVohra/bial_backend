# Generated by Django 3.2.16 on 2023-08-01 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_remove_employeeprofile_is_team_lead'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeprofile',
            name='team',
        ),
    ]
