# Generated by Django 2.1.5 on 2019-01-24 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTeamapp', '0037_auto_20190122_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='Pic',
            field=models.FileField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 24, 10, 51, 50, 395381)),
        ),
    ]
