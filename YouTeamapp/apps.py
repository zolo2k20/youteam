# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class YouteamappConfig(AppConfig):
    name = 'YouTeamapp'

    # This function is the only new thing in this file
    # it just imports the signal file when the app is ready
    def ready(self):
        import YouTeamapp.signals
