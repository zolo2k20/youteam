# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-11 07:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTeamapp', '0013_auto_20190111_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devloperuser',
            name='password',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='devloperuser',
            name='username',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 11, 7, 24, 35, 351963)),
        ),
    ]
