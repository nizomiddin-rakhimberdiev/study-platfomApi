# Generated by Django 4.2.6 on 2023-10-12 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studyPlatformApi', '0022_rename_video_links_themevideolink_links'),
    ]

    operations = [
        migrations.RenameField(
            model_name='themevideolink',
            old_name='links',
            new_name='video_links',
        ),
    ]
