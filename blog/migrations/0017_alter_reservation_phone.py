# Generated by Django 3.2.15 on 2022-09-30 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_reservation_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
