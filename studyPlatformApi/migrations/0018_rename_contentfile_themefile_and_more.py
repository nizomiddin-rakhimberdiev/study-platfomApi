# Generated by Django 4.2.6 on 2023-10-12 16:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studyPlatformApi', '0017_remove_contentfile_content_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContentFile',
            new_name='ThemeFile',
        ),
        migrations.RenameModel(
            old_name='ContentImage',
            new_name='ThemeImage',
        ),
        migrations.RenameModel(
            old_name='ContentVideoLink',
            new_name='ThemeVideoLink',
        ),
        migrations.AddField(
            model_name='theme',
            name='text',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Content text'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='themefile',
            name='content',
            field=models.ManyToManyField(related_name='files', to='studyPlatformApi.theme'),
        ),
        migrations.AlterField(
            model_name='themeimage',
            name='content',
            field=models.ManyToManyField(related_name='images', to='studyPlatformApi.theme'),
        ),
        migrations.AlterField(
            model_name='themevideolink',
            name='content',
            field=models.ManyToManyField(related_name='links', to='studyPlatformApi.theme'),
        ),
        migrations.DeleteModel(
            name='Content',
        ),
    ]
