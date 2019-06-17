# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from YouTeamapp.models import *
from YouTeamapp.forms import *
# Register your models here.
class profileAdmin(admin.ModelAdmin):
    list_display=['Pic','Datetime','cover','Designation','complete_project','salary_year','salary_month','salary_hour','City','State','Zip_code','offical_email','LinkedIn_profile_url']

    serch_field=['name']

class technologyAdmin(admin.ModelAdmin):
    list_display=['programing_language','expirencepl','framework','expirencefw','frontend_technology','expirenceft','data_base','expirencedb','other_skills','expirenceos','development_tools','operating_system']

admin.site.register(devoloperprofile,profileAdmin)
admin.site.register(devlopertechnical, technologyAdmin)
