# Generated by Django 2.2.28 on 2023-01-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20230123_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='url',
            field=models.URLField(default=''),
        ),
    ]
