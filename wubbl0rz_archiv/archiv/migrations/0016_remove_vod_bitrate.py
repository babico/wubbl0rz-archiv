# Generated by Django 4.0 on 2021-12-18 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0015_alter_apistorage_broadcaster_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vod',
            name='bitrate',
        ),
    ]
