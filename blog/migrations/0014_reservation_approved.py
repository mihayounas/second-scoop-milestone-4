# Generated by Django 3.2.15 on 2022-09-27 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_reservation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
