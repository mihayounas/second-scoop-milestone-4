# Generated by Django 3.2.15 on 2022-10-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0048_auto_20221023_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]