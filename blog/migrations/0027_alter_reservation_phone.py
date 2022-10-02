# Generated by Django 3.2.15 on 2022-10-02 14:50

import django.core.validators
from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20221002_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, default=12345678910, max_length=31, validators=[django.core.validators.RegexValidator('\\s*\\(?0\\d{4}\\)?(\\s*|-)\\d{3}(\\s*|-)\\d{3}\\s*)|(\\s*\\(?0\\d{3}\\)?(\\s*|-)\\d{3}(\\s*|-)\\d{4}\\s*)|(\\s*(7|8)(\\d{7}|\\d{3}(\\-|\\s{1})\\d{4})\\s*')]),
            preserve_default=False,
        ),
    ]
