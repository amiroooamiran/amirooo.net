# Generated by Django 4.2.4 on 2023-11-27 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_learn_by_updates_read_updates_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='updates',
            name='link',
        ),
        migrations.RemoveField(
            model_name='updates',
            name='previev',
        ),
    ]
