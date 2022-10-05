# Generated by Django 3.2.15 on 2022-10-05 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0035_alter_reservation_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_profile',
            field=models.OneToOneField(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
