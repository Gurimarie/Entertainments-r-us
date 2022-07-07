""" Apps-file for checkout-app """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ docstring """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """ override default ready-method """
        import checkout.signals
