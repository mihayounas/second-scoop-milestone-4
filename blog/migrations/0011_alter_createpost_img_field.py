# Generated by Django 3.2.15 on 2022-09-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_post_img_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='img_field',
            field=models.ImageField(blank=True, upload_to='cloudinary://493494235994288:zTTpGxQKi__Q5xN5tStvSY1DDRA@df4j1glpo'),
        ),
    ]
