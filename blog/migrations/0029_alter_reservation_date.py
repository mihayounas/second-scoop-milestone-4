# Generated by Django 3.2.15 on 2022-10-03 10:45

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_alter_reservation_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date.today), django.core.validators.RegexValidator('(\\d{4})-(\\d{2})-(\\d{2})')]),
        ),
    ]
