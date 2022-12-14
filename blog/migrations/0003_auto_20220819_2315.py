# Generated by Django 3.2.15 on 2022-08-19 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_reservations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservations',
            old_name='body',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='reservations',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_reservations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='date',
            field=models.DateField(),
        ),
    ]
