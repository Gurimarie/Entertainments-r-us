""" app-file for the performances-app """
from django.apps import AppConfig


class PerformancesConfig(AppConfig):
    """ a class for the performances-app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'performances'
