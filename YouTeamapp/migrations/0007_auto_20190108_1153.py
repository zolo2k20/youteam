# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-08 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTeamapp', '0006_auto_20190108_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
                ('expirence', models.IntegerField()),
                ('frameworke', models.CharField(max_length=200)),
                ('frontend_technology', models.CharField(max_length=200)),
                ('data_base', models.CharField(max_length=200)),
                ('other', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_letter', models.TextField()),
                ('language', models.CharField(max_length=200)),
                ('frameworke', models.CharField(max_length=200)),
                ('frontend_technology', models.CharField(max_length=200)),
                ('data_base', models.CharField(max_length=200)),
                ('other', models.CharField(max_length=200)),
                ('java', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='devsign',
        ),
        migrations.DeleteModel(
            name='expirence',
        ),
    ]
