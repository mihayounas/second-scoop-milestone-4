# Generated by Django 3.2.15 on 2022-09-30 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_reservation_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
