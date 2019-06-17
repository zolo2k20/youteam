from django.contrib.auth.models import User
from YouTeamapp.models import *
import django_filters

class TechnologyFilter(django_filters.FilterSet):
    class Meta:
        model = devlopertechnical
        fields = ['programing_language', 'expirencepl', 'framework','expirencefw','frontend_technology','expirenceft','data_base','expirencedb','development_tools','operating_system' ]
