# Generated by Django 4.2.6 on 2023-10-30 18:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studyPlatformApi', '0029_alter_category_image_course_category_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='category_images/', verbose_name='Category Image'),
            preserve_default=False,
        ),
    ]
