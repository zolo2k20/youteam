# Generated by Django 2.1.5 on 2019-01-21 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTeamapp', '0030_auto_20190121_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technology',
            name='Category',
        ),
        migrations.AlterField(
            model_name='profile',
            name='Datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 21, 12, 3, 37, 601630)),
        ),
    ]
