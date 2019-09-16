from django.apps import AppConfig
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from gaana.signals import create_profile,save_profile


class GaanaConfig(AppConfig):

    name = 'gaana'

    def ready(self):
        import profile.signals

