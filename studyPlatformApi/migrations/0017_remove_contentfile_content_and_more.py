# Generated by Django 4.2.6 on 2023-10-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyPlatformApi', '0016_alter_content_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentfile',
            name='content',
        ),
        migrations.RemoveField(
            model_name='contentimage',
            name='content',
        ),
        migrations.RemoveField(
            model_name='contentvideolink',
            name='content',
        ),
        migrations.AddField(
            model_name='contentfile',
            name='content',
            field=models.ManyToManyField(related_name='files', to='studyPlatformApi.content'),
        ),
        migrations.AddField(
            model_name='contentimage',
            name='content',
            field=models.ManyToManyField(related_name='images', to='studyPlatformApi.content'),
        ),
        migrations.AddField(
            model_name='contentvideolink',
            name='content',
            field=models.ManyToManyField(related_name='links', to='studyPlatformApi.content'),
        ),
    ]