# Generated by Django 2.1.5 on 2019-01-14 10:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('YouTeamapp', '0016_auto_20190114_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tech',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='YouTeamapp.technology'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 14, 10, 37, 12, 459430)),
        ),
    ]
