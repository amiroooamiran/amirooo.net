# Generated by Django 4.2.4 on 2024-01-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='select',
            field=models.BooleanField(default=False),
        ),
    ]