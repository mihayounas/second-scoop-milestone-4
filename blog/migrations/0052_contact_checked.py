# Generated by Django 3.2.15 on 2022-10-26 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0051_contact_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
