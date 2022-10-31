""" apps-file for the profiles-app """
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """ a class for the profiles-app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
