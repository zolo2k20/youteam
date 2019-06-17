# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.conf import settings

    #Title=models.CharField(max_length=250)

class devlopertechnical(models.Model):
    programing_language=models.CharField(max_length=100)
    user_exp = models.ForeignKey(User,on_delete=models.CASCADE,primary_key=True)
    expirencepl=models.CharField(max_length=3,null=True)
    framework=models.CharField(max_length=200)
    expirencefw=models.CharField(max_length=3,null=True)
    frontend_technology=models.CharField(max_length=200)
    expirenceft=models.CharField(max_length=3,null=True)
    data_base=models.CharField(max_length=200)
    expirencedb=models.CharField(max_length=3,null=True)
    other_skills=models.CharField(max_length=200)
    expirenceos=models.CharField(max_length=3,null=True)
    development_tools=models.CharField(max_length=200,null=True)
    operating_system=models.CharField(max_length=200,null=True)
class devoloperprofile(models.Model):
    Pic=models.FileField(upload_to="images/",null=True)
    customer = models.ForeignKey(User,on_delete=models.CASCADE,primary_key=True)
    #name=models.ForeignKey(programing_language,on_delete=models.CASCADE,null=True)
    Datetime=models.DateTimeField(default=datetime.now(),blank=True)
    Designation=models.CharField(max_length=100)
    complete_project=models.CharField(max_length=100)
    salary_year=models.FloatField(null=True)
    salary_month=models.FloatField(null=True)
    salary_hour=models.FloatField(null=True)
    City=models.CharField(max_length=100,null=True)
    State=models.CharField(max_length=100,null=True)
    Zip_code=models.CharField(max_length=10,null=True)
    offical_email=models.CharField(max_length=80,null=False)
    LinkedIn_profile_url=models.CharField(max_length=100,null=True)
    cover=models.TextField(null=True)
    def get_absolute_url(self):
     return reverse('YouTeamapp:edit', kwargs={'pk': self.pk})

class clientprofile(models.Model):
    Pic=models.FileField(upload_to="images/",null=True)
    contact_person=models.CharField(max_length=200,null=True)
    business_name=models.CharField(max_length=300,null=True)
    Street_address=models.CharField(max_length=300,null=True)
    City=models.CharField(max_length=100,null=True)
    State=models.CharField(max_length=100,null=True)
    Zip_code=models.CharField(max_length=10,null=True)
    offical_email=models.CharField(max_length=80,null=True)
    LinkedIn_profile_url=models.CharField(max_length=100,null=True)
    Specific_Registration_Details=models.TextField(null=True)



class Freemodel(models.Model):
    Empolyee_name=models.CharField(max_length=50)
    Compny_name=models.CharField(max_length=100)
    email=models.EmailField()
