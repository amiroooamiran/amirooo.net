# Generated by Django 4.2.4 on 2023-09-23 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_rename_chapter_title_chapter_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='chapter_videos',
        ),
        migrations.RemoveField(
            model_name='video',
            name='course',
        ),
    ]
