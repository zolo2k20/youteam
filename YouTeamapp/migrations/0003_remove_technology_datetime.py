# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-04 12:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('YouTeamapp', '0002_auto_20190104_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technology',
            name='Datetime',
        ),
    ]
