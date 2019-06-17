# Generated by Django 2.1.5 on 2019-01-22 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTeamapp', '0034_auto_20190121_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientprofile',
            name='VAT_number',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='business_legal_type',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='company_phone',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='company_url',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='incorporated_country',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='incorporated_state',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='state',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='street_address',
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='City',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='LinkedIn_profile_url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='Specific_Registration_Details',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='State',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='Street_address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='business_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='contact_person',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='offical_email',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='Zip_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 22, 10, 6, 42, 326860)),
        ),
    ]