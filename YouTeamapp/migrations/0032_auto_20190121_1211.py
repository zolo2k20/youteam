# Generated by Django 2.1.5 on 2019-01-21 12:11

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('YouTeamapp', '0031_auto_20190121_1203'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='technology',
            new_name='devlopertechnology',
        ),
        migrations.AlterField(
            model_name='profile',
            name='Datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 21, 12, 11, 29, 467265)),
        ),
    ]
