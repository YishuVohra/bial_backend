# Generated by Django 3.2.16 on 2023-07-31 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_familyprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyprofile',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
