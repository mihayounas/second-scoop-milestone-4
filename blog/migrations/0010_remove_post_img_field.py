# Generated by Django 3.2.15 on 2022-09-20 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20220920_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img_field',
        ),
    ]
