# Generated by Django 4.1.7 on 2023-06-11 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('da_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dauser',
            name='last_login',
        ),
    ]
