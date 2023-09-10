# Generated by Django 4.2.4 on 2023-09-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_nikname_user_profile'),
        ('courses', '0004_course_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='resource',
        ),
        migrations.AddField(
            model_name='course',
            name='Star',
            field=models.ManyToManyField(related_name='Star', to='user.user'),
        ),
        migrations.AddField(
            model_name='course',
            name='likes',
            field=models.ManyToManyField(related_name='Likes', to='user.user'),
        ),
        migrations.AddField(
            model_name='video',
            name='resource',
            field=models.FileField(blank=True, upload_to='course/resource'),
        ),
        migrations.AlterField(
            model_name='course',
            name='banner',
            field=models.ImageField(blank=True, upload_to='course/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
