# Generated by Django 2.1.5 on 2019-01-14 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTeamapp', '0017_auto_20190114_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 14, 10, 37, 21, 491459)),
        ),
    ]