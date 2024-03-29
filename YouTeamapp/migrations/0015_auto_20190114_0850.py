# Generated by Django 2.1.5 on 2019-01-14 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTeamapp', '0014_auto_20190111_0724'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('street_address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('Zip_code', models.CharField(max_length=20)),
                ('company_phone', models.CharField(max_length=15)),
                ('company_url', models.CharField(max_length=100)),
                ('business_legal_type', models.CharField(max_length=500)),
                ('incorporated_country', models.CharField(max_length=100)),
                ('incorporated_state', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('VAT_number', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='DevloperUser',
        ),
        migrations.AlterField(
            model_name='profile',
            name='Datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 14, 8, 50, 39, 83519)),
        ),
    ]
