""" app-file for home-app """
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """ class for home-page """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
