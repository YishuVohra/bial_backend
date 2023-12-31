# Generated by Django 3.2.16 on 2023-08-02 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userpermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='RolePermissionsMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userpermission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userrole')),
            ],
            options={
                'db_table': 'user_role_permission_mapping',
                'unique_together': {('role', 'permission')},
            },
        ),
    ]
