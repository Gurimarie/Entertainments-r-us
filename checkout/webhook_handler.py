""" to handle Stripe webhooks (messages about stripe-events) """
import json
import time
from django.http import HttpResponse

from performances.models import Product
from .models import Order, OrderLineItem


class StripeWH_Handler:
    """ a class to handle Stripe webhooks """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ handle generic/unknown/unexpected webhook-event """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ handle payment_intent.succeeded webhook-event from Stripe """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        order_total = round(intent.charges.data[0].amount / 100, 0)

        """ to create clean data (no empties) in the shipping-details """
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    order_total__iexact=shipping_details.order_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, quantity in json.loads(bag).items():
                    # orig. item_data is quantity&size. Not applicable.

                    product = Product.objects.filter(pk=item_id)
                    # or: product = get_object_or_404(Product, pk=item_id)?

                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Order created in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ handle payment_intent.failed webhook-event from Stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
