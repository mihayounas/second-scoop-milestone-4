# Generated by Django 3.2.15 on 2022-08-19 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220819_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservations',
            name='reservations',
        ),
    ]
