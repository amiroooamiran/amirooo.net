# Generated by Django 4.2.4 on 2023-08-08 05:35

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, null=True)),
                ('description', tinymce.models.HTMLField(null=True)),
                ('price', models.IntegerField(default=0.0)),
                ('discount', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('resource', models.FileField(upload_to='course/resource')),
                ('length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Learning',
            fields=[
                ('courseproperty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.courseproperty')),
            ],
            bases=('courses.courseproperty',),
        ),
        migrations.CreateModel(
            name='Prerequisite',
            fields=[
                ('courseproperty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.courseproperty')),
            ],
            bases=('courses.courseproperty',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('courseproperty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.courseproperty')),
            ],
            bases=('courses.courseproperty',),
        ),
    ]
