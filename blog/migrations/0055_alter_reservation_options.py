# Generated by Django 3.2.15 on 2023-04-12 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0054_comment_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['created_at']},
        ),
    ]