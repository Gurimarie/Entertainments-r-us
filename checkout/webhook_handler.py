""" to handle Stripe webhooks (messages about stripe-events) """
from django.http import HttpResponse


class StripeWH_Handler:
    """ a class to handle Stripe webhooks """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ handle generic/unknown/unexpected webhook-event """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
