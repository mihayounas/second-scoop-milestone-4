# Generated by Django 3.2.15 on 2022-10-02 15:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_alter_reservation_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^((\\+44)|(0)) ?\\d{4} ?\\d{6}$')]),
        ),
    ]
