# Generated by Django 3.2.15 on 2022-10-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_alter_post_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='number_of_people',
            field=models.PositiveIntegerField(default='1'),
            preserve_default=False,
        ),
    ]
