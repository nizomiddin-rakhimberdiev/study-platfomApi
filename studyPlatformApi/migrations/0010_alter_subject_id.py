# Generated by Django 4.2.6 on 2023-10-11 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyPlatformApi', '0009_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
